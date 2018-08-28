#! /api/server/questions/schema.py
# -*- coding: utf-8 -*-
"""Contains the schema for the questions endpoint
Marshmallow validation with wtforms
"""

from marshmallow import Schema, fields
from marshmallow_validators.wtforms import from_wtforms
from wtforms.validators import Length


class QuestionsSchema(Schema):
    """Questions schema"""
    question_id = fields.Str(dump_only=True)
    title = fields.Str(
        required=True,
        validate=from_wtforms(
            [
                Length(
                    min=20,
                    max=100,
                    message="Question title should be between 20 to 50 characters"
                ),
            ]
        )
    )
    details = fields.Str(
        required=True,
        validate=from_wtforms(
            [
                Length(min=50, max=500,
                       message="Details should be between 50 to 500 characters"),
            ]
        )
    )
