#! /api/server/config.py
# -*- coding: utf-8 -*-
"""This is the config module
This module contains classes for our various configuration settings.
"""

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:  # pylint: disable=too-few-public-methods
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'TheSecretKey')
    JWT_SECRET_KEY = os.getenv('SECRET_KEY', 'TheSecretKey')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    DATABASE_HOST = "localhost"
    SWAGGER = {
        "title": "Stack Overflow",
        "uiversion": 2,
    }


class DevelopmentConfig(BaseConfig):  # pylint: disable=too-few-public-methods
    """Development configuration."""
    TESTING = False
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    DATABASE_NAME = os.getenv("PGDATABASE")
    DATABASE_USER = os.getenv("PGUSER")
    DATABASE_PASS = os.getenv("PGPASSWORD")
    DATABASE_HOST = os.getenv("PGHOST")
    DATABASE_PORT = os.getenv("PGPORT")


class TestingConfig(BaseConfig):  # pylint: disable=too-few-public-methods
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DATABASE_NAME = os.getenv("PGDATABASE") +"_test"


class ProductionConfig(BaseConfig):  # pylint: disable=too-few-public-methods
    """Production configuration."""
    SECRET_KEY = 'TheSecretKey'
    DEBUG = False
    DATABASE_NAME = os.getenv("PGDATABASE")