#! /api/server/request/models.py
# -*- coding: utf-8 -*-
"""This is the request modules
This module contains functions that are used in the auth endpoint
"""
from api.server.helpers import get_query, run_query, get_just_query


def create_question(input_title, input_details, user_id):
    """Create a new question"""
    try:
        query = (u"INSERT INTO tbl_questions (question_title, "
                 "question_details, posted_by) VALUES (%s,%s,%s) "
                 ";")
        inputs = input_title, input_details, user_id
        return run_query(query, inputs)
    except psycopg2.Error as e:
        print(e)


def get_all_questions():
    """Get all questions asked"""
    query = ("SELECT * FROM tbl_questions;")
    user_reqeusts = get_just_query(query)
    return user_reqeusts

def get_single_question(id):
    """Gets a single question asked"""
    query = ("SELECT * FROM tbl_questions WHERE question_id = %s;")
    inputs = id
    user_requests = get_query(query, inputs)
    return user_requests

def delete_single_question(id):
    """Delete a question"""
    query = ("DELETE FROM tbl_questions WHERE questions_id = %s;")
    inputs = id
    user_requests = run_query(query, inputs)
    return user_requests
