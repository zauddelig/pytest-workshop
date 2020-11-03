"""
I was requested to created an authenticator mechanism.
For business reasons I'm bound to use a mongodb database.

Here is what I come up, can you help me find the defects and test this class?
"""
from pymongo.database import Database


class Users:
    """ This class will create a database connection. """

    def __init__(self, database: Database):
        self.collection = database.users

    def _get_password(self, username):
        return self.collection.find_one({'username': username})['password']

    def authenticate(self, username: str, password: str):
        user_password = self._get_password(username)
        return user_password == password

    def insert_user(self, username: str, password: str):
        self.collection.insert_one({
            'password': password,
            'username': username
        })
