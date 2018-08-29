#! /api/server/answers/schema.py
# -*- coding: utf-8 -*-
"""Contains the schema for the questions endpoint
Marshmallow validation with wtforms
"""

from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Length


class Answerschema(Schema):
    """Questions schema"""
    question_id = fields.Str(dump_only=True)
    
    answer = fields.Str(
        required=True,
        validate=from_wtforms(
            [
                Length(min=50, max=500,
                       message="Details should be between 10 to 500 characters"),
            ]
        )
    )
