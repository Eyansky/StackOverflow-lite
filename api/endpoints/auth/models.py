#! /api/endpoints/auth/models.py
# -*- coding: utf-8 -*-
"""This is the auth modules
This module contains functions that are used in the auth endpoint
"""
from api.endpoints import APP, BCRYPT
from api.endpoints.resources.helpers import run_query, get_query


def signup_user(first_name, last_name, email, password):
    """Create a new user account"""
    # encrypt the password
    hash_password = BCRYPT.generate_password_hash(
        password, APP.config.get('BCRYPT_LOG_ROUNDS')
    ).decode()

    # query and the user inputs
    query = (u"INSERT INTO tbl_users (first_name, last_name, email, password, "
             ") VALUES (%s, %s, %s, %s);")
    inputs = first_name, last_name, email, hash_password
    # run query
    return run_query(query, inputs)

def email_exists(input_email):
    """Check if the user email exists"""
    # SQL query
    query = u"SELECT * FROM tbl_users WHERE email = %s;"
    inputs = input_email
    all_users = get_query(query, inputs)

    for find_email in all_users:
        if find_email['email'] == inputs:
            return True
    return False


def check_email_for_login(input_email):
    """Return user email"""
    # SQL query
    query = u"SELECT * FROM tbl_users WHERE email = %s;"
    inputs = input_email
    all_users = get_query(query, inputs)

    for find_email in all_users:
        if find_email['email'] == input_email:
            return find_email


def login_user(input_email, input_password):
    """Log in user function"""
    logging_user_details = check_email_for_login(input_email)
    if BCRYPT.check_password_hash(logging_user_details['password'],
                                  input_password):
        # compare password input to saved password
        return logging_user_details
    return False
