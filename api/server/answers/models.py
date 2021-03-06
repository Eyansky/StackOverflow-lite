#! /api/server/request/models.py
# -*- coding: utf-8 -*-
"""This is the request modules
This module contains functions that are used in the auth endpoint
"""
from api.server.helpers import get_query, run_query, get_just_query

class Answer():

    def create_answer(self,user_id, question_id, answer):
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

    def get_all_answers(self,id):
        """Get all answers asked"""
        query = ("SELECT * FROM tbl_answers WHERE question = %s;")
        inputs = id 
        answers = get_query(query, inputs)
        return answers

    def question_exists(self,question_id):
        """Check if the user email exists"""
        # SQL query
        query = u"SELECT * FROM tbl_questions WHERE question_id = %s;"
        inputs = question_id
        all_questions = get_query(query, inputs)

        for find_question in all_questions:
            if find_question['question_id'] == inputs:
                return True
        return False

    def get_specific_answer(self, id):
        """Get specific"""
        query = ("SELECT answered_by FROM tbl_answers WHERE answer_id = %s;")
        inputs = id 
        answer = get_query(query, inputs)
        return answer

    def update_answer(self, answer, answer_id):
        "Update answer details"
        query = ("UPDATE tbl_answers SET answer_details = %s WHERE answer_id = %s;")
        inputs = answer, answer_id
        run_query(query,inputs)
        return True

    def update_correct(self, correct, answer_id):
        "Update answer correctness"
        query = ("UPDATE tbl_answers SET is_correct = %s WHERE answer_id = %s;")
        inputs = correct, answer_id
        x = run_query(query,inputs)
        return x

    def get_correctness(self, id):
        """Get state of correctness"""
        query = ("SELECT is_correct FROM tbl_answers WHERE answer_id = %s;")
        inputs = id 
        correct = get_query(query, inputs)
        return correct

    def get_voters(self):
        """Get who voted"""
        query = ("SELECT voter_user_id FROM tbl_voters;")
        correct = get_just_query(query)
        return correct

    def add_vote(self,upvote):
        """Add votes """
        try:
            query = ("INSERT INTO tbl_answers ( upvote ) VALUES (%s) ;")
            inputs = upvote
            return run_query(query, inputs)
        except psycopg2.Error as e:
            print(e)

    def delete_vote(self, id):
        """Delete an upvote"""
        query = ("DELETE FROM tbl_answers WHERE question_id = %s;")
        inputs = id
        user_requests = run_query(query, inputs)
        return user_requests

    def chukua_votes(self, answer_id):
        """Get the votes"""
        query = ("SELECT upvote FROM tbl_answers WHERE answer_id = %s;")
        inputs = answer_id
        correct = get_query(query, inputs)
        return correct 