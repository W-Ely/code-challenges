"""Counting Duplicates Tests."""
from counting_duplicates import duplicate_count


def test_duplicate_count_0_0():
    assert duplicate_count("abcde") == 0


def test_duplicate_count_0_1():
    assert duplicate_count("abcdea") == 1


def test_duplicate_count_0_2():
    assert duplicate_count("indivisibility") == 1


def test_duplicate_count_0_3():
    assert duplicate_count("abcdea") == 1
