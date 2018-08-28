# db_con.py
"""This module connects to the database"""
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from connect_creds import CONNECT_CREDS

credentials = CONNECT_CREDS
print(credentials)
class DbConn(object):
    """Database Creation Class"""
    def __init__(self):
        """Constructor method"""
        self.conn = connect(**credentials)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def query(self, query):
        """Query execution method"""
        self.cur.execute(query)

    def close(self):
        """Close Connection"""
        self.cur.close()
        self.conn.close()
