#! /api/endpoints/resources/__init__.py
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

# instanciate Flask
APP = Flask(__name__)

# os.getenv -> return the value of the environment variable
APP_SETTINGS = os.getenv(
    'APP_SETTINGS',
    'api.endpoints.resources.config.DevelopmentConfig'
)
# retreiving config stored in separate files (config.py)
APP.config.from_object(APP_SETTINGS)

# import blueprintS
from api.endpoints.questions.views import QUESTIONS_BLUEPRINT
from api.endpoints.answers.views import ANSWERS_BLUEPRINT

# Register Blueprints
APP.register_blueprint(QUESTIONS_BLUEPRINT)
APP.register_blueprint(ANSWERS_BLUEPRINT)
