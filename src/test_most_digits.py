"""Most Digits Test."""
from most_digits import find_longest


def test_most_digits_0_0():
    assert find_longest([1, 10, 100]) == 100


def test_most_digits_0_1():
    assert find_longest([9000, 8, 800]) == 9000


def test_most_digits_0_2():
    assert find_longest([8, 900, 500]) == 900


def test_most_digits_0_3():
    assert find_longest([3, 40000, 100]) == 40000


def test_most_digits_0_4():
    assert find_longest([1, 200, 100000]) == 100000


def test_most_digits_0_5():
    assert find_longest([1, 123, 1234, 4321]) == 1234
