# ! /api/tests/test_answers.py
# -*- coding: utf-8 -*-
"""Tests for the answers endpoint
"""

import json
import unittest
from flask_jwt_extended import (create_access_token)

from db_conn import DbConn
from api.tests.base import BaseTestCase, truncate_tables

URL_PREFIX = "/api/v2/users/questions"


def create_user():
    """Create a user in the DB"""
    db_instance = DbConn()
    query = (u"INSERT INTO tbl_users (user_id, first_name, last_name, "
             "email, password) VALUES (%s,%s,%s,%s,%s);")
    inputs = '988', 'User', 'User', 'user@user.com', 'aaaAAA111'
    db_instance.cur.execute(query, inputs)
    db_instance.conn.commit()
    db_instance.close()


def create_question(self, title, details):
    """New Question"""

    # Create a UserObject for tokens
    user = {
        "user_id": "988",
        "user_email": "email@mail.com"
    }
    access_token = create_access_token(identity=user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    return self.client.post( URL_PREFIX,
        data=json.dumps(dict(
            title=title,
            details=details
        )),
        content_type='application/json',
        headers=headers
    )

def create_answer(self, answer):
    """New answer"""

    # Create a UserObject for tokens
    user = {
        "user_id": "567",
        "user_email": "email@mail.com"
    }
    access_token = create_access_token(identity=user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    return self.client.post(
        URL_PREFIX + '/1/answers',
        data=json.dumps(dict(
            answer=answer
        )),
        content_type='application/json',
        headers=headers
    )


class TestAnswersEndpoint(BaseTestCase):
    """Class that handles Answers Endpoint test"""

    def test_failing_post_answer(self):
        """ test failing post answer """
        with self.client:
            # First add a question then add an answer to the question.
            title = "Test title for question"
            details = "This is the sample question. Do you have any doubts about it?"

            q = create_question(self,title, details)
            answer = "This is the answer you have been looking for. Happy hacking."
            response = create_answer(self, answer )
            data = json.loads(response.data.decode())
            # self.assertEqual(data["msg"] == "Answer has been posted")
            self.assertEqual(response.status_code, 422)
            truncate_tables()
    
    def test_invalid_question_for_answer(self):
        with self.client:
            response = self.client.get(
                URL_PREFIX + '/900/answers',)
            self.assertEqual(response.status_code, 422)
            truncate_tables()