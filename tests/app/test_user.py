from app.user import Users
from mongomock import MongoClient
import pytest
from collections import namedtuple


@pytest.fixture
def user():
    user = namedtuple('user', ['username', 'password'])
    return user('username', 'password')

@pytest.fixture()
def connection_fixture(user):
    username = 'Test Username'
    password = 'Test Password'
    a_users = Users(MongoClient().users)
    a_users.insert_user(*user)
    return a_users


class TestAuthenticate():

    def test_authenticate_success(self, connection_fixture, user):
        authenticated = connection_fixture.authenticate(*user)
        assert authenticated == True

    def test_authenticate_failure(self, connection_fixture, user):
        authenticated = connection_fixture.authenticate(user.username, 'other password')
        assert authenticated == False

    def test_no_username(self, connection_fixture, user):
        authenticated = connection_fixture.authenticate('mocke', user.password)
        assert authenticated == False

class TestInsertUser():
    pass
