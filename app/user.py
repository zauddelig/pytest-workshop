"""
I was requested to created an authenticator mechanism.
For business reasons I'm bound to use an sqlite3 database.

Here is what I come up, can you help me find the defects and test this class?
"""
from mongomock.database import Database


class Users:
    """ This class will create a database connection. """
    CREATE = "CREATE TABLE users (username text, password text);"
    INSERT = "INSERT INTO users (username, password) VALUES (?, ?);"
    GET_PASSWORD = "SELECT password FROM users WHERE username=?;"

    def __init__(self, database: Database):
        self.collection = database.users

    def _get_password(self, username):
        user = self.collection.find_one({'username': username})
        if (user is not None):
            return user['password']
        return None

    def authenticate(self, username: str, password: str):
        user_password = self._get_password(username)
        return user_password is not None and user_password == password

    def insert_user(self, username: str, password: str):
        self.collection.insert_one({'password': password, 'username': username})
