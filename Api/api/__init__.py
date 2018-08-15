#! /api/endpoints/__init__.py
"""
This is the core module
This module does imports flask framework, initializes it and passes the
initialized flask object to various modules and extensions.
"""
# the os module provides a portable way of using operating system dependent functionality
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

# import auth blueprints
from api.endpoints.questions.views import QUESTIONS_BLUEPRINT 

# Register Blueprints
APP.register_blueprint(QUESTIONS_BLUEPRINT)