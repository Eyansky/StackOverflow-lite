#! /api/server/answers/views.py
# -*- coding: utf-8 -*-
"""This is the answers module
This module contains various routes for the answers endpoint
"""

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)
from flasgger.utils import swag_from

from api.server.answers.schema import Answerschema
from api.server.answers.models import ( create_answer, chukua_votes, get_voters, get_correctness, update_correct, get_all_answers, question_exists, get_specific_answer, update_answer )

# Create a blueprint
# __name__ . It is a built-in variable that returns the name of the module. 
ANSWERS_BLUEPRINT = Blueprint(
    'answer', __name__, url_prefix='/api/v2/users/questions/<int:id>')

# Instanciate marshmallow shemas
ANSWER_SCHEMA = Answerschema()

class AnswersAPI(MethodView):
    """User Answers resource"""
    @jwt_required
    @swag_from('documentation/create_answer.yml', methods=['POST'])
    def post(self,id):  # pylint: disable=R0201
        """Send POST method to answers endpoint"""

        # get the post data
        post_data = request.get_json()

        # load input to the marshmallow schema
        try:
            ANSWER_SCHEMA.load(post_data)

        # return error object case there is any
        except ValidationError as err:
            response_object = {
                'status': 'fail',
                'msg': 'Validation errors.',
                'errors': err.messages
            }
            return make_response(jsonify(response_object)), 422
        
        # check if the id exists
        if question_exists(id) == True:

            # If no validation errors
            current_user = get_jwt_identity()
            # Get input data as dictionary

            answer = post_data.get('answer')
            user_id = current_user["user_id"]
            question_id = id 

            #send to db
            create_answer( user_id, question_id, answer )
           
            response_object = {
                "status": 'success',
                "msg": "Answer has been posted"
            }
            return make_response(jsonify(response_object)), 201
        else:
            response = {
                "error":"Question does not exist"
            }
            return make_response(jsonify(response)), 422

    @swag_from('documentation/get_all_answers.yml', methods=['GET'])
    def get(self, id):
        """Get all answers for specific question"""
        # check if email exists
        if question_exists(id) == True:
            response_object = {
                "status": 'success',
                "questions": get_all_answers(id)
            }
            return make_response(jsonify(response_object)), 200
        else:
            response = {
                "error":"Question does not exist"
            }
            return make_response(jsonify(response)), 422

class EditAnswersAPI(MethodView):
    """User Answers resource"""
    @jwt_required
    @swag_from('documentation/modify_answer.yml', methods=['PUT'])
    def put(self,id,answer_id):  # pylint: disable=R0201
        """Send put method to answers endpoint"""
        # getting the user id
        current_user = get_jwt_identity()
        user_id = current_user["user_id"]
        
        # checking if user is related to the answer they want to post
        dbuser = get_specific_answer(answer_id)

        for key in dbuser:
            if str(key["answered_by"]) == str(user_id):
                if question_exists(id) == True:
                    # get the post data
                    post_data = request.get_json()

                    # load input to the marshmallow schema
                    try:
                        ANSWER_SCHEMA.load(post_data)

                    # return error object case there is any
                    except ValidationError as err:
                        response_object = {
                            'status': 'fail',
                            'msg': 'Validation errors.',
                            'errors': err.messages
                        }
                        return make_response(jsonify(response_object)), 422
                    
                    #Updating the answer 
            
                    answer = post_data.get('answer')

                    update_answer(answer, answer_id)

                    response = {
                        "message":"Question has been updated"
                    }
                    return make_response(jsonify(response)), 201
                
                else:
                    response = {
                        "error":"Question does not exist"
                    }
                    return make_response(jsonify(response)), 422
            else:
                response = {"error":"Only the owner can edit this."}
                return make_response(jsonify(response)), 401


class CorrectAnswersAPI(MethodView):
    """User Answers resource"""
    @jwt_required
    @swag_from('documentation/correct_answer.yml', methods=['PUT'])
    def put(self,id,answer_id):  # pylint: disable=R0201
        """Send put method to answers endpoint"""
        # getting the user id
        current_user = get_jwt_identity()
        user_id = current_user["user_id"]
        
        # checking if user is related to the answer they want to edit
        dbuser = get_specific_answer(answer_id)

        for key in dbuser:
            if str(key["answered_by"]) == str(user_id):

                # Checking if the state is YES or NO
                state = get_correctness(answer_id)

                if question_exists(id) == True:
                    for key in state:
                        if str(key["is_correct"]) == "No":
                            correct= "Yes"
                            update_correct(correct, answer_id)
                        else:
                            correct= "No"
                            update_correct(correct, answer_id)

                    response = {
                        "message":"Question has been marked as correct"
                    }
                    return make_response(jsonify(response)), 201
            
                else:
                    response = {
                        "error":"Question does not exist"
                    }
                    return make_response(jsonify(response)), 422
            else:
                response = {"error":"Only the owner can edit this."}
                return make_response(jsonify(response)), 401

# class upvoteAPI(MethodView):
#     """User Answers resource"""
#     @jwt_required
#     @swag_from('documentation/modify_answer.yml', methods=['PUT'])
#     def put(self,id,answer_id):  # pylint: disable=R0201
#         """Send put method to answers endpoint"""
#         # getting the user id
#         current_user = get_jwt_identity()
#         user_id = current_user["user_id"]
#         # check if user voted
#         mtu = get_voters()
#         votes = chukua_votes(answer_id) 
        
#         if mtu:
#             for find_voters in mtu:
#                 if find_voters['voter_user_id'] == user_id:
#                     print("You already voted")
#                     response = {"details":"umepiga kura"}
#                     return make_response(jsonify(response)), 401

#                 else:
#                     if votes:
#                         for kura in votes:
#                             iebc = kura["upvote"]
#                             print(iebc)
#                             response = {"details":iebc}
#                             return make_response(jsonify(response)), 401
                    

            

#         response = {"details":"Keep calm!!"}
#         return make_response(jsonify(response)), 401


        

# define API resources
ANSWERS_VIEW = AnswersAPI.as_view('answers_api')
EDIT_ANSWER = EditAnswersAPI.as_view("edit_api")
CORRECT_ANSWER = CorrectAnswersAPI.as_view("correct_api")
# UPVOTE_ANSWER = upvoteAPI.as_view("upvote_api")

# add rules for endpoints
ANSWERS_BLUEPRINT.add_url_rule(
    '/answers',
    view_func=ANSWERS_VIEW,
    methods=['POST','GET']
)

# add rules for endpoints
ANSWERS_BLUEPRINT.add_url_rule(
    '/answers/<int:answer_id>',
    view_func=EDIT_ANSWER,
    methods=['PUT']
)

# add rules for endpoints
ANSWERS_BLUEPRINT.add_url_rule(
    '/answers/<int:answer_id>/correct',
    view_func=CORRECT_ANSWER,
    methods=['PUT']
)

# add rules for endpoints
# ANSWERS_BLUEPRINT.add_url_rule(
#     '/answers/<int:answer_id>/upvote',
#     view_func=UPVOTE_ANSWER,
#     methods=['PUT']
# )