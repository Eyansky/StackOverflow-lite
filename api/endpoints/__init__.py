#! /api/endpoints/__init__.py
# -*- coding: utf-8 -*-
"""This is the core module

This module does imports flask framework, initializes it and passes the
initialized flask object to various modules and extensions.
"""

# the os module provides a portable way of using operating system dependent
# functionality
import os

# python microframework
from flask import Flask
# provides bcrypt hashing utilities for our application
from flask_bcrypt import Bcrypt

# TOKEN
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)

# instanciate Flask
APP = Flask(__name__)

# os.getenv -> return the value of the environment variable
APP_SETTINGS = os.getenv(
    'APP_SETTINGS',
    'api.endpoints.resources.config.DevelopmentConfig'
)
# retreiving config stored in separate files (config.py)
APP.config.from_object(APP_SETTINGS)

# pass flask app object to Bcrypt
BCRYPT = Bcrypt(APP)
JWT = JWTManager(APP)

# token setup
@JWT.user_claims_loader
def add_claims_to_access_token(user):
    """Function that will be called whenever create_access_token is used"""
    return {'email': user["user_email"]}


@JWT.user_identity_loader
def user_identity_lookup(user):
    """Define token identity"""
    return user["user_id"]

# import blueprints
from api.endpoints.auth.views import AUTH_BLUEPRINT
from api.endpoints.questions.views import QUESTIONS_BLUEPRINT
from api.endpoints.answers.views import ANSWERS_BLUEPRINT

# Register Blueprints
APP.register_blueprint(AUTH_BLUEPRINT)
APP.register_blueprint(QUESTIONS_BLUEPRINT)
APP.register_blueprint(ANSWERS_BLUEPRINT)
