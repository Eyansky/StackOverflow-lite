#! /api/endpoints/answers/models.py
# -*- coding: utf-8 -*-
"""This is the auth modules
This module contains functions that are used in the auth endpoint
"""
from api.endpoints import APP
from api.endpoints.resources.helpers import run_query, get_query

def answers(id, jibu):
    # query and the user inputs
    query = ("INSERT INTO tbl_answers (answers_id, answers_status) VALUES (%s, %s);")
          
    inputs = id, jibu
    # run query
    run_query(query, inputs)
    return True


def updateanswers(id, jibu):
    # query and the user inputs
    query = (u"UPDATE tbl_requests SET request_title=%s,request_description=%s WHERE request_id=%s AND created_by=%s ;")
          
    inputs = id, jibu
    # run query
    run_query(query, inputs)
    return True
