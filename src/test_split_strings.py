"""Split Strings Tests."""
import pytest
from split_strings import solution


tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
    ("asdfasdfd", ['as', 'df', 'as', 'df', 'd_'])
)


@pytest.mark.parametrize("string, expected", tests)
def test_split_strings_0_0(string, expected):
    """Several tests of strings"""
    assert solution(string) == expected
