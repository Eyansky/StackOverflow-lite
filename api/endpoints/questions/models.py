#! /api/endpoints/questions/models.py
# -*- coding: utf-8 -*-
"""This is the auth modules
This module contains functions that are used in the auth endpoint
"""
from api.endpoints import APP
from api.endpoints.resources.helpers import run_query, get_query, run_just_query, get_just_query


def view_questions():
    """Get all questions"""
    # query and the user inputs
    query = ("SELECT * FROM tbl_questions;")
    # run query
    return run_just_query(query)

def singleQuestion(id):
    """ Get single question"""
    # query and the user inputs
    query = ("SELECT tbl_users.email, "
             "tbl_questions.questions_id, "
             "tbl_questions.questions_title, "
             "tbl_questions.questions_description, "
             "FROM tbl_users, tbl_questions "
             "WHERE tbl_users.user_id = tbl_questions.created_by "
             "AND tbl_questions.created_by = %s;")

    single_Question = get_query(query, id)
    return single_Question

def addQuestion(title, question):
    """ Add question """
    # query and the user inputs
    query = ("INSERT INTO tbl_questions (questions_title, questions_description) VALUES (%s, %s);")

    inputs = title, question
    # run query
    print (run_query(query, inputs))
    return True

def deleteQuestion(question_id):
    # query and the user inputs
    query = ("DELETE FROM tbl_questions WHERE questions_id = %s;")

    inputs = question_id
    # run query
    run_query(query, inputs)
    return True
