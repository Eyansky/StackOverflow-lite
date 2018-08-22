#! /api/endpoints/auth/views.py
# -*- coding: utf-8 -*-
"""This is the auth module
This module contains various routes for the auth endpoint
"""

from flask import Blueprint, make_response, jsonify, request
from flask.views import MethodView
from marshmallow import ValidationError
from flask_jwt_extended import (create_access_token)

from api.endpoints.auth.models import signup_user, email_exists
from api.endpoints.auth.schema import UserSchema

# Create a blueprint
AUTH_BLUEPRINT = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

# Instanciate marshmallow schemas
USER_SCHEMA = UserSchema()


class SignupAPI(MethodView):
    """User Signup resource"""
    def post(self):  # pylint: disable=R0201
        """POST method"""
        # get the post data
        post_data = request.get_json()

        # check for no input i.e. {}
        if not post_data:
            response_object = {
                'status': 'fail',
                'msg': 'No input data provided.'
            }
            return make_response(jsonify(response_object)), 400

        try:
            USER_SCHEMA.load(post_data)

        # return error object case there is any
        except ValidationError as err:
            response_object = {
                'status': 'fail',
                'msg': 'Validation errors.',
                'errors': err.messages
            }
            return make_response(jsonify(response_object)), 422
        # Store user input in variables
        input_first_name = post_data.get('first_name')
        input_last_name = post_data.get('last_name')
        input_email = post_data.get('email')
        input_password = post_data.get('password')

        if email_exists(input_email):
            response_object = {
                "status": "fail",
                "msg": "Sorry! Email '{}' already exists.".format(
                    input_email)
            }
            return make_response(jsonify(response_object)), 422

        signup_user(input_first_name, input_last_name,
                    input_email, input_password)
        # return response 
        response_object = {
            "status": 'success',
            "msg": "Account for '{}' has been created.".format(
                input_email),
            "user": {
                "first_name": input_first_name,
                "last_name": input_last_name,
                "email": input_email
            }

        }
        return make_response(jsonify(response_object)), 201


# define API resources
SIGNUP_VIEW = SignupAPI.as_view('signup_api')

# add rules for auth enpoints
AUTH_BLUEPRINT.add_url_rule(
    '/signup',
    view_func=SIGNUP_VIEW,
    methods=['POST']
)
