#! /api/server/__init__.py
# -*- coding: utf-8 -*-
"""This is the core module

This module does imports flask framework, initializes it and passes the
initialized flask object to various modules and extensions.
"""

# the os module provides a portable way of using operating system dependent
# functionality
import os

# python microframework
from flask import Flask, redirect, jsonify

# provides bcrypt hashing utilities for our application
from flask_bcrypt import Bcrypt

# TOKEN
from flask_jwt_extended import JWTManager, jwt_required

# making cross-origin AJAX possible
from flask_cors import CORS
from flasgger import Swagger

# instanciate Flask
APP = Flask(__name__)

# initialize the Flask-Cors extension with default arguments in order
# to allow CORS for all domains on all routes
CORS(APP)

# os.getenv -> return the value of the environment variable
APP_SETTINGS = os.getenv(
    'APP_SETTINGS',
    'api.server.config.DevelopmentConfig'
)
# retreiving config stored in separate files (config.py)
APP.config.from_object(APP_SETTINGS)

# blacklisting tokens
APP.config['JWT_BLACKLIST_ENABLED'] = True
APP.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
# pass flask app object to Bcrypt
BCRYPT = Bcrypt(APP)
JWT = JWTManager(APP)
SWAG = Swagger(
    APP,
    template={
        "swagger": "2.0",
        "uiversion": 2,
        "info": {
            "title": "Stack Overflow - LITE",
            "version": "2.0",
        },
        "consumes": [
            "application/x-www-form-urlencoded",
        ],
        "produces": [
            "application/json",
        ],
    },
)

# blacklisting tokens
blacklist = set()

@JWT.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@APP.route('/')
def home():
    return redirect('/apidocs')

APP.url_map.strict_slashes = False


# import auth blueprints
from api.server.auth.views import AUTH_BLUEPRINT  # noqa  # pylint: disable=C0413
from api.server.questions.views import QUESTIONS_BLUEPRINT  # noqa  # pylint: disable=C0413
from api.server.answers.views import ANSWERS_BLUEPRINT  # noqa  # pylint: disable=C0413

# Register Blueprints
APP.register_blueprint(AUTH_BLUEPRINT)
APP.register_blueprint(QUESTIONS_BLUEPRINT)
APP.register_blueprint(ANSWERS_BLUEPRINT)


@APP.errorhandler(404)
def page_not_found(error):
    response = {"message":"page not found!!!"}
    return jsonify(response), 404

@APP.errorhandler(500)
def internal_server_error(error):
    response = {"message": "Our server is encountering a problem handling this page."}
    return jsonify(response), 500

@APP.errorhandler(403)
def forbidden(error):
    response = {"message": "You do not have permission to access this resource!"}
    return jsonify(response), 403

@APP.errorhandler(405)
def method_not_allowed(error):
    response = {"message": "This method is not allowed, Please check again!"}
    return jsonify(response), 405

# Endpoint for revoking the current users access token
@APP.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200