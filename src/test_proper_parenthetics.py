"""Module tests proper_paranthetics kata."""
from proper_parenthetics import proper_paranthetics


def test_correct_order():
    """Test return 0 for balanced."""
    assert proper_paranthetics('()()()') == 0


def test_incorrect_order_open():
    """Test return 1 for open."""
    assert proper_paranthetics('()()(') == 1


def test_broken():
    """Test return -1 for balanced."""
    assert proper_paranthetics(')()()') == -1
