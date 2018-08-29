#! /api/server/request/models.py
# -*- coding: utf-8 -*-
"""This is the request modules
This module contains functions that are used in the auth endpoint
"""
from api.server.helpers import get_query, run_query, get_just_query


def create_answer(user_id, question_id, answer):
    """Create a new answer"""
    try:
        upvote = 0
        downvote = 0
        query = (u"INSERT INTO tbl_answers (answered_by, "
                 "question, answer_details, upvote, downvote ) VALUES (%s,%s,%s, %s,%s) "
                 ";")
        inputs = user_id, question_id, answer, upvote, downvote
        return run_query(query, inputs)
    except psycopg2.Error as e:
        print(e)

def get_all_answers(id):
    """Get all answers asked"""
    query = ("SELECT * FROM tbl_answers WHERE question = %s;")
    inputs = id 
    answers = get_query(query, inputs)
    return answers

def question_exists(question_id):
    """Chek if the user email exists"""
    # SQL query
    query = u"SELECT * FROM tbl_questions WHERE question_id = %s;"
    inputs = question_id
    all_questions = get_query(query, inputs)

    for find_question in all_questions:
        if find_question['question_id'] == inputs:
            return True
    return False