"""
Conftests is used to define plugins and fixtures that may be used through out
 all tests.
"""
import pytest


@pytest.fixture(autouse=True)
def assert_true():
    """ This fixture will run everytime at each test invocatation """
    assert True


@pytest.fixture
def assert_false():
    """
    This fixture will be available to all tests,
     but it will not run every time """
    assert False, "You called it!"
