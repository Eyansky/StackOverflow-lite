#! /api/server/questions/views.py
# -*- coding: utf-8 -*-
"""This is the questions module
This module contains various routes for the questions endpoint
"""

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)
from flasgger.utils import swag_from

from api.server.questions.schema import QuestionsSchema
from api.server.questions.models import (
    create_question, get_all_questions, get_single_question, delete_single_question)

# Create a blueprint
# __name__ . It is a built-in variable that returns the name of the module. 
QUESTIONS_BLUEPRINT = Blueprint(
    'question', __name__, url_prefix='/api/v2/users/')

# Instanciate marshmallow shemas
QUESTION_SCHEMA = QuestionsSchema()


class QuestionsAPI(MethodView):
    """User Questions resource"""
    @jwt_required
    @swag_from('documentation/create_questions.yml', methods=['POST'])
    def post(self):  # pylint: disable=R0201
        """Send POST method to questions endpoint"""

        # get the post data
        post_data = request.get_json()

        # load input to the marshmallow schema
        try:
            QUESTION_SCHEMA.load(post_data)

        # return error object case there is any
        except ValidationError as err:
            response_object = {
                'status': 'fail',
                'msg': 'Validation errors.',
                'errors': err.messages
            }
            return make_response(jsonify(response_object)), 422

        # If no validation errors
        current_user = get_jwt_identity()
        # Get input data as dictionary

        input_title = post_data.get('title')
        input_details = post_data.get('details')
        user_id = current_user["user_id"]

        create_question(input_title, input_details, user_id)

        response_object = {
            "status": 'success',
            "msg": "Question successfully posted."
        }
        return make_response(jsonify(response_object)), 201

    @swag_from('documentation/get_all_questions.yml', methods=['GET'])
    def get(self):
        """Get all questions"""

        response_object = {
            "status": 'success',
            "questions": get_all_questions()
        }
        return make_response(jsonify(response_object)), 200

class SingleQuestionsAPI(MethodView):
    """User single Question resource"""
    @swag_from('documentation/get_single_questions.yml', methods=['GET'])
    def get(self,id):
        """Get a single question"""

        try:
            if int(id):
                response_object = {
                    "status": 'success',
                    "question": get_single_question(id)
                }
                return make_response(jsonify(response_object)), 200
          
        except ValueError:
            return jsonify({"error": "Only integers are required"})
            
    @swag_from('documentation/delete_single_questions.yml', methods=['GET'])
    def delete(self,id):
        """Delete a single question"""

        try:
            if int(id):
                response_object = {
                    "status": 'success'
                }
                return make_response(jsonify(response_object)), 200
          
        except ValueError:
            return jsonify({"error": "Only integers are required"})

# define API resources
QUESTIONS_VIEW = QuestionsAPI.as_view('questions_api')
SINGLE_QUESTIONS_VIEW = SingleQuestionsAPI.as_view('single_questions_api')

# add rules for questions endpoints
QUESTIONS_BLUEPRINT.add_url_rule(
    '/questions',
    view_func=QUESTIONS_VIEW,
    methods=['POST', 'GET']
)

# add rules for single questions endpoints
QUESTIONS_BLUEPRINT.add_url_rule(
    '/questions/<id>',
    view_func=SINGLE_QUESTIONS_VIEW,
    methods=[ 'GET','DELETE']
)
