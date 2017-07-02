"""Module tests forbes kata."""
from forbes import forbes


def test_forbes_returns_correct_information():
    """Test correct information is returned."""
    assert forbes() == """
Oldest: Name: Phil Knight, Net Worth: 24400000000, Industry: Nike
Youngest: Name: Mark Zuckerberg, Net Worth: 44600000000, Industry: Facebook
"""
