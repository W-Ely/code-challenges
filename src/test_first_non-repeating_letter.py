"""First non-repeating letter tests."""
from first_non_repeating_letter import first_non_repeating_letter


def test_first_non_repeating_letter_0_0():
    """Basic Tests."""
    assert first_non_repeating_letter('a') == 'a'
    assert first_non_repeating_letter('stress') == 't'
    assert first_non_repeating_letter('moonmen') == 'e'


def test_first_non_repeating_letter_0_1():
    """Handle empty strings."""
    assert first_non_repeating_letter('') == ''


def test_first_non_repeating_letter_0_2():
    """Handle all repeating strings."""
    assert first_non_repeating_letter('abba') == ''
    assert first_non_repeating_letter('aa') == ''


def test_first_non_repeating_letter_0_3():
    """Handle odd characters."""
    assert first_non_repeating_letter('~><#~><') == '#'
    assert first_non_repeating_letter('hello world, eh?') == 'w'


def test_first_non_repeating_letter_0_4():
    """Handle letter cases."""
    assert first_non_repeating_letter('sTreSS') == 'T'
    assert first_non_repeating_letter(
        'Go hang a salami, I\'m a lasagna hog!') == ','


def test_first_non_repeating_letter_0_5():
    """Handle a little something of mine."""
    assert first_non_repeating_letter('XYZZY') == 'X'
