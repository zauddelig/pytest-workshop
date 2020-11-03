"""
Pytest allows us run our tests with multiple parameters

This will usually improve the code re-usage and lean up the code significantly.

"""
import pytest


@pytest.mark.parametrize('number', [1, 2])
def test_squared_is_less_than_tripled(number):
    """
    In this case we prove that a number multiplied by three is bigger than the
    same number squared.

    We are cherry picking our test to make so that they pass,
     can you prove otherwise?
    """
    assert number * 3 > number ** 2, "You found it!"


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
