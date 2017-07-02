"""Module tests forbes kata."""
from forbes import DATA
from forbes import forbes


def test_forbes_returns_correct_information():
    """Test original information returns correct results."""
    assert forbes() == """
Oldest: Name: Phil Knight, Net Worth: 24400000000, Industry: Nike
Youngest: Name: Mark Zuckerberg, Net Worth: 44600000000, Industry: Facebook
"""


def test_again_remove_previous_two():
    """Test diffrent information returns correct results."""
    DATA.remove(DATA[5])
    DATA.remove(DATA[-17])
    assert forbes() == """
Oldest: Name: Carlos Slim Helu, Net Worth: 50000000000, Industry: telecom
Youngest: Name: Sergey Brin, Net Worth: 34400000000, Industry: Google
"""
