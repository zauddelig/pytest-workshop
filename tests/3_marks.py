"""
Pytest allows us to mark our tests, this may create additional behaviour.

Marks are:
 - skip: skip a test
 - skpif: condirtionally skip a test
 - usefixtures: uses a fixture even if it is not declared by the test
 - parametrize
 - flagging tests
"""
import pytest
import os


@pytest.mark.skip
def test_skip_mark():
    """
    The skip mark will always skip a test.
    """
    assert False, "This test will be skipped"


@pytest.mark.skipif(
    'MY_DATABASE' not in os.environ, reason='Database must be specified!')
def test_skipif_mark():
    """
    The skipif mark will conditionally skip a test, this usually is used to
     check a precondition, like a machine specific setup.
    """
    assert False, "MY_DATABASE environment variable exists!"


@pytest.mark.parametrize('number', [1, 2])
def test_format_and_f_strings(number):
    """
    Parametrize will run the test for each argument, in this case it will
     ran twice
    """
    assert f'number is {number}' == 'number is {number}'.format(number=number)


@pytest.mark.parametrize(
    'input, output', [
        ['abcd', 4],
        ['abcde', 5],
    ]
)
def test_multiple_parameters(input, output):
    """
    We can send multiple parameters to the test using parametrize.
    Frequently this may be useful to test the input/output of a function.
    """
    assert len(input) == output


@pytest.mark.parametrize(
    'input, output', [
        ['abcd', 4],
        ['abcde', 5],
    ]
)
class TestParametrize:
    """
    Parametrize works even inside classes!
    """
    def test_multiple_parameters(self, input, output):
        assert len(input) == output


# =========
# EXERCISE
# We set the pytest cli to run only some marked test or exclude them,
# try:
# pytest  tests/3_marks.py -m slow
# pytest  tests/3_marks.py -m "not slow"
# =========

@pytest.mark.slow
def test_slow():
    assert True, 'slow runs'


# =========
# EXERCISE
# Sometimes tests maybe misleading
# even thought we have full coverage there may be corner cases
# that we are not testing.
# =========


def aways_true(number: int):
    """
    This function always return True.
    Of course the square of a number is always bigger than its doubling.
    """
    return number * 2 < number ** 2


@pytest.mark.parametrize('number', [1, 4, 5, 10, 20, 100])
def test_squared_is_less_than_tripled(number):
    """
    We are cherry picking our test to make so that they pass,
     can you prove otherwise?
    """
    assert aways_true(number), "You found it!"
