"""
Main Test  for users
"""

import json
import unittest
from api.endpoints import APP


class TestUsers(unittest.TestCase):
    """
        Test Users
    """

    def setUp(self):
        """
        code that is executed before each test
        """
        app.testing = True
        self.app = app.test_client()
        self.data = {
            "firstname": "Ian",
            "lastname": "Mwangi",
            "email": "ian@eyansky.com",
            "password": "qwerty"
        }

        self.error_data = {
            "firstname": "mwangi",
            "lastname": "wairimu",
            "email": "mwangi@mwangi.com",
            "username": "mwangi",
            "password": "x"
        }

        self.user = {
            "username": "wairimu",
            "password": "wairimu"
        }

        self.error_user = {
            "username": "wairimu",
            "password": "qwerty"
        }

    def test_register(self):
        """
        Test for successful registration
        """
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.data),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(response.status_code, 201)

    def test_view_all_users(self):
        """
        Test for view all users
        """
        response = self.app.get('api/v1/auth/signup',
                                data=json.dumps(self.data),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        """
        Test for successful Login
        """
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.user),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_errorlogin(self):
        """
        Test for invalid Login
        """
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.error_user),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()