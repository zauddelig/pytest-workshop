"""
We can define our own fixtures, these are custom functions that are decorated
 with pytest.fixture

They can be used passing them as arguments in our tests.

"""
import pytest
from unittest import mock


class Calculator:
    _cache = None

    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second

    def _complex_calculation(self) -> int:
        return self.first + self.second

    def calculate(self) -> int:
        if self._cache is None:
            self._cache = self._complex_calculation()
        return self._cache


@pytest.fixture
def monkeypatch_complex_calculation(monkeypatch):
    """
    Our fixtures can use previously defined fixtures,
    this allows us to create specialized fixtures without reinventing the wheel
     """
    value_to_return = 1
    monkeypatch.setattr(
        Calculator, '_complex_calculation', mock.Mock(
            return_value=value_to_return))
    return value_to_return


def test_complex_calculation_call(monkeypatch_complex_calculation: int):
    """
    In this case, the complex calculation is mocked completely.

    As you can see the argument will hold the return of the fixture.

    In this case we are testing that, missing the cache,
     we will call the complex calculation.
    """
    calculator = Calculator(1, 2)
    calculator.calculate()
    assert monkeypatch_complex_calculation == 1
    assert calculator._cache == monkeypatch_complex_calculation

    # in this case the test consists on the call to this protected method.
    calculator._complex_calculation.assert_called_once_with()


@pytest.fixture
def monkeypatch_cache(monkeypatch_complex_calculation):
    """
    In some cases we can yield a result
     this allows us to cleanup our result or prepare our tests

    In this case we are setting the cache to a know value
     and restoring it later on
    """
    calculator = Calculator(1, 2)
    old_cache = calculator._cache
    calculator._cache = monkeypatch_complex_calculation
    yield calculator
    Calculator._cache = old_cache


def test_cache(monkeypatch_cache: Calculator):
    """
    The return will hold the yield of the fixture.

    In this case we are testing that if the cache is not null we will not do
     the complex calculation.
    """
    assert monkeypatch_cache.calculate() == monkeypatch_cache._cache
    monkeypatch_cache._complex_calculation.assert_not_called()


# ===========
# Exercise
# How we can test this class?
# what defects does it have?
# ===========

import sqlite3


class Users:
    """ This class will create a database connection. """
    CREATE_QUERY = "CREATE TABLE users (username test, password text)"

    def __init__(self, connection: sqlite3.Connection):
        self.cursor = connection.cursor()

    def _get_password(self, username):
        self.cursor.execute(
            "SELECT password WHERE username=? from users", username)
        return self.cursor.fetchone()

    def authenticate(self, username: str, password: str):
        return self._get_password(username) == password


