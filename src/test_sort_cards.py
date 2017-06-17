"""Tests for sort_cards module."""
from sort_cards import sort_cards


def test_sort_cards_0_0():
    assert sort_cards(list('39A5T824Q7J6K')) == list('A23456789TJQK')


def test_sort_cards_0_2():
    assert sort_cards(list('Q286JK395A47T')) == list('A23456789TJQK')


def test_sort_cards_0_3():
    assert sort_cards(list('54TQKJ69327A8')) == list('A23456789TJQK')


def test_sort_cards_0_4():
    assert sort_cards(
        list('54TQKJ69327A854TQKJ69327A854TQKJ69327A8')
    ) == list('AAA222333444555666777888999TTTJJJQQQKKK')
