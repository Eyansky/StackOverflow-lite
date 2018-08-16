#! /api/endpoints/questions/views.py
# -*- coding: utf-8 -*-
"""
This is the questions module

This module contains various routes for the questions endpoint
"""

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from api.endpoints.resources.models import (
    view_questions)

# Create a blueprint
QUESTIONS_BLUEPRINT = Blueprint('questions', __name__, url_prefix='/api/v1/users')

class Questions(MethodView):
    """Questions """

    def get(self):
        return jsonify({'questions': view_questions()}), 200
    
    

# define API resources
QUESTIONS_VIEW = Questions.as_view('questions_api')

# add rules for Questions endpoints
QUESTIONS_BLUEPRINT.add_url_rule(
    '/questions',
    view_func=QUESTIONS_VIEW,
    methods=['GET']
)

