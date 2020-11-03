"""
I was requested to created an authenticator mechanism.
For business reasons I'm bound to use an sqlite3 database.

Here is what I come up, can you help me find the defects and test this class?
"""
import sqlite3


class Users:
    """ This class will create a database connection. """
    CREATE = "CREATE TABLE users (username test, password text);"
    INSERT = "INSERT INTO users VALUES (?, ?);"
    GET_PASSWORD = "SELECT password WHERE username=? from users;"

    def __init__(self, connection: sqlite3.Connection):
        self.cursor = connection.cursor()

    def _get_password(self, username):
        self.cursor.execute(
            self.GET_PASSWORD, username)
        return self.cursor.fetchone()

    def authenticate(self, username: str, password: str):
        return self._get_password(username) == password

    def insert_user(self, username: str, password: str):
        self.cursor.execute(self.INSERT, [password, username])
