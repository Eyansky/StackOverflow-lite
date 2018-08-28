# ! /api/tests/test_test.py
# -*- coding: utf-8 -*-
"""Tests for the auth endpoint
Contains basic tests for registration, login and logout
"""

import json
import unittest
from flask_jwt_extended import (create_access_token)

from db_conn import DbConn
from api.tests.base import BaseTestCase, truncate_tables

URL_PREFIX = "/api/v2/users/"


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
    """New request"""

    # Create a UserObject for tokens
    user = {
        "user_id": "988",
        "user_email": "email@mail.com"
    }
    access_token = create_access_token(identity=user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    return self.client.post(
        URL_PREFIX + 'questions',
        data=json.dumps(dict(
            title=title,
            details=details
        )),
        content_type='application/json',
        headers=headers
    )


class TestQuestionsEndpoint(BaseTestCase):
    """Class that handles Questions Endpoint test"""

    def test_get_user_info(self):
        """Test for successful retreival of logged in user info"""
        with self.client:
            create_user()
            # Create a UserObject for tokens
            user = {
                "user_id": "988",
                "user_level": "User"
            }
            access_token = create_access_token(identity=user)
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            response = self.client.get(
                "/api/v2/auth/user", headers=headers)
            self.assertEqual(response.status_code, 200)
            truncate_tables()

    def test_successful_question(self):
        """Test for successful question submission"""
        with self.client:
            response = create_question(
                self,
                "This is the request title. Short and descriptive",
                ("The description. It has lengths that need to be adhered to. "
                 "The description. It has lengths that need to be adhered to. "
                 "The description. It has lengths that need to be adhered to. "
                 "The description. It has lengths that need to be adhered to.")
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['msg'] ==
                            'Question successfully posted.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)
            truncate_tables()

    def test_validation_errors(self):
        """Test for presence of validation error
        This case short body length
        """
        with self.client:
            response = create_question(
                self,
                "This is the request title. Short and descriptive",
                "Body goes here"
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['msg'] == 'Validation errors.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 422)
            truncate_tables()

    def test_get_all_questions(self):
        """Test any user can see all question"""
        with self.client:
            response = self.client.get(
                URL_PREFIX + 'questions',)
            self.assertEqual(response.status_code, 200)
            truncate_tables()

    def test_get_single_question(self):
        """Test any user can see a single question"""
        title = "Test question"
        details = "This is a test question. Isnt it?"
        create_question(self, title, details)
        with self.client:
            response = self.client.get(
                URL_PREFIX + 'questions/1',)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            truncate_tables()

    def test_fail_get_single_question(self):
        """Test for error url"""
        with self.client:
            response = self.client.get(
                URL_PREFIX + 'questions/x',)
            data = json.loads(response.data.decode())
            self.assertTrue(data["error"] == "Only integers are required")
            truncate_tables()
  
    def test_delete_question(self):
        """Test any user can see a single question"""
        title = "Test question"
        details = "This is a test question. Isnt it?"
        create_question(self, title, details)
        with self.client:
            response = self.client.delete(
                URL_PREFIX + 'questions/1',)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["status"] == "success")
            truncate_tables()  
    
    def test_fail_delete_question(self):
        """Test for error url"""
        with self.client:
            response = self.client.delete(
                URL_PREFIX + 'questions/x',)
            data = json.loads(response.data.decode())
            self.assertTrue(data["error"] == "Only integers are required")
            truncate_tables()
