#! /api/endpoints/answers/views.py
# -*- coding: utf-8 -*-
"""
This is the answers module

This module contains various routes for the answers endpoint
"""

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from api.endpoints.answers.models import (answers, updateanswers)

# Create a blueprint
ANSWERS_BLUEPRINT = Blueprint('answers', __name__, url_prefix='/api/v1/users/')


class addAnswer(MethodView):
    """
    Add answer
    """

    def is_valid(self, item):
        """
            checking for valid credentials
        """
        errors = {}
        if not item.get("answer"):
            errors['answer'] = "Answer is required"

        return len(errors) == 0, errors

    def post(self, id):
        """add an answer"""
        if request.is_json:
            valid, errors = self.is_valid(request.json)
            if not valid:
                return {"data": errors, "status": "error"}, 400
            #
            result = request.json
            jibu = result['answer']

            answers(id, jibu)
            return jsonify({"message": "answers has been added!!"}), 201

class updateAnswer(MethodView):
    """
    Update answer
    """

    def is_valid(self, item):
        """
            checking for valid credentials
        """
        errors = {}
        if not item.get("answer"):
            errors['answer'] = "Answer is required"

        return len(errors) == 0, errors

    def put(self, id):
        """add an answer"""
        if request.is_json:
            valid, errors = self.is_valid(request.json)
            if not valid:
                return {"data": errors, "status": "error"}, 400
            #
            result = request.json
            jibu = result['answer']

            updateanswers(id, jibu)
            return jsonify({"message": "answers has been Updated!!"}), 201


# define API resources
ANSWERS_VIEW = addAnswer.as_view('answers_api')

# add rules for answers endpoints
ANSWERS_BLUEPRINT.add_url_rule(
    '/questions/<int:id>/answers',
    view_func=ANSWERS_VIEW,
    methods=['POST']
)
