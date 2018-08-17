"""
Main Test  for questions
"""

import json
import unittest

from api.endpoints import APP


class TestQuestions(unittest.TestCase):
    """
        Test questions endpoint
    """

    def setUp(self):
        """
        code that is executed before each test
        """
        APP.testing = True
        self.APP = APP.test_client()
        self.question = {
            "title" : "Eyansky",
            "question" : "why is my name Linda? Do you know the answer to my question?"
        }
        self.answers = {"answer":"This is a sample answer!!!"}
        

    def test_view_all_questions(self):
        """
        Test for view all questions
        """
        response = self.APP.get('/api/v1/users/questions')
        self.assertEqual(response.status_code, 200)
    
    def test_view_single_question(self):
        """
        Test for view single question
        """
        response = self.APP.get('/api/v1/users/questions/1')
        self.assertEqual(response.status_code, 200)
    
    def test_add_question(self):
        """
        Test for successful add question
        """
        response = self.APP.post('/api/v1/users/questions',
                                 data=json.dumps(self.question),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
    
    def test_add_answer(self):
        """
        Test for successful add answer
        """
        response = self.APP.post('/api/v1/users/questions/1/answers',
                                 data=json.dumps(self.answers),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
    


if __name__ == "__main__":
    unittest.main()