"""
A python file must contain a prefix to be detected by pytest as a test file.


You can run the test using:
pytest tests/must_have_a_prefx.py


To allow pytest to find this file add the test_ prefix, e.g.:

test_basics.py


once done you can run it using:
pytest test.py
"""

def test_assertions():
    """
    Most of the times we will use assertions to run our tests.

    An assert accepts a boolean value, either True or False.

    Most of the times we have a single assert, but we can use more than one.

    If the value:
        - is True the test is considered passed
        - is False the test is considered failing

    Make this test pass,
    """
    assert False, "Fix me"


def test_one_is_two():
    """
    This will raise an assertion error:

    E       AssertionError: One is not two!
    E       assert 1 == 2

    When the test passes the message will not contribute to the noise.

    As exercise try to fix this test.
    """
    assert 1 == 2, 'One is not two!'


def this_will_not_run():
    """
    To run this function needs to have the test_ prefix, e.g.:

    As exercise try to rename this test.
    """
    assert False, "This will not fail"

