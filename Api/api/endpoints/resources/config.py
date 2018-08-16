#! /api/endpoints/resources/config.py
# -*- coding: utf-8 -*-
"""This is the config module
This module contains classes for our various configuration settings.
"""

import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:  # pylint: disable=too-few-public-methods
    """Base configuration."""
    DEBUG = False


class DevelopmentConfig(BaseConfig):  # pylint: disable=too-few-public-methods
    """Development configuration."""
    DEBUG = True


class TestingConfig(BaseConfig):  # pylint: disable=too-few-public-methods
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False