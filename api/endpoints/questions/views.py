#! /api/endpoints/questions/views.py
# -*- coding: utf-8 -*-
"""
This is the questions module

This module contains various routes for the questions endpoint
"""

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView 
from api.endpoints.questions.models import ( view_questions, singleQuestion, addQuestion, deleteQuestion)

# Create a blueprint
QUESTIONS_BLUEPRINT = Blueprint(
    'questions',
    __name__,
    url_prefix='/api/v1/users/')


class Questions(MethodView):
    """Questions """

    def is_valid(self, item):
        """
            checking for valid credentials
        """
        errors = {}
        if not item.get("title"):
            errors['title'] = "Title is required"

        if not item.get("question"):
            errors['question'] = "Question is required"
        elif len(item.get("question")) < 15:
            errors["question"] = "Question must have more than 15 characters. Enhance it please"

        return len(errors) == 0, errors

    def get(self):
        return jsonify({'questions': view_questions()}), 200

    def post(self):
        """add a question"""
        if request.is_json:
            valid, errors = self.is_valid(request.json)
            if not valid:
                return {"data": errors, "status": "error"}, 400
           
            result = request.json
            title = result['title']
            question = result['question']

            swali = addQuestion(title, question)
            if swali:
                return jsonify({"message": "Question has been added!!"}), 201
            else:
                response = {"error":"Question has not been added"}
                return response, 400


class SingleQuestion(MethodView):
    """ Get single question """

    def get(self, id):
        try:
            if int(id):
                question = singleQuestion(str(id))
                return jsonify({"question": question})
        
        except ValueError:
            return jsonify({"error": "Only integers are required"})

    def delete(self, id):
        try:
            if int(id):
                question = deleteQuestion(str(id))
                response = {"question": "question has been deleted!!"}
                return response, 200
        
        except ValueError:
            response = {"error": "Only integers are required"}
            return response, 401

# define API resources
QUESTIONS_VIEW = Questions.as_view('questions_api')
SINGLEQUESTION_VIEW = SingleQuestion.as_view("SingleQuestion_api")

# add rules for Questions endpoints
QUESTIONS_BLUEPRINT.add_url_rule(
    '/questions',
    view_func=QUESTIONS_VIEW,
    methods=['GET','POST']
)

# add rules for Questions endpoints
QUESTIONS_BLUEPRINT.add_url_rule(
    '/questions/<id>',
    view_func=SINGLEQUESTION_VIEW,
    methods=['GET']
)
