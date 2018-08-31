#! /api/server/request/models.py
# -*- coding: utf-8 -*-
"""This is the request modules
This module contains functions that are used in the auth endpoint
"""
from api.server.helpers import get_query, run_query, get_just_query

class Questions():

    def create_question(self, input_title, input_details, user_id):
        """Create a new question"""
        try:
            query = (u"INSERT INTO tbl_questions (question_title, "
                    "question_details, posted_by) VALUES (%s,%s,%s) "
                    ";")
            inputs = input_title, input_details, user_id
            return run_query(query, inputs)
        except psycopg2.Error as e:
            print(e)


    def get_all_questions(self):
        """Get all questions asked"""
        query = ("SELECT * FROM tbl_questions;")
        user_reqeusts = get_just_query(query)
        return user_reqeusts

    def get_single_question(self, id):
        """Gets a single question asked"""
        query = ("SELECT * FROM tbl_questions WHERE question_id = %s;")
        inputs = id
        user_requests = get_query(query, inputs)
        return user_requests

    def delete_single_question(self, id):
        """Delete a question"""
        query = ("DELETE FROM tbl_questions WHERE question_id = %s;")
        inputs = id
        deleted = run_query(query, inputs)
        return deleted

    def get_specific_question(self, id):
        """Get specific question"""
        query = ("SELECT posted_by FROM tbl_questions WHERE question_id = %s;")
        inputs = id 
        question = get_query(query, inputs)
        return question
