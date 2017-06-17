"""Tests for string pyramid module."""


def test_watch_pyramid_from_the_side_0_0():
    """Three digit string."""
    from string_pyramid import watch_pyramid_from_the_side
    result = watch_pyramid_from_the_side('abc')
    expected = '  c  \n bbb \naaaaa'
    assert result == expected


def test_watch_pyramid_from_the_side_0_1():
    """Five digit string."""
    from string_pyramid import watch_pyramid_from_the_side
    result = watch_pyramid_from_the_side('abcde')
    expected = '    e    \n   ddd   \n  ccccc  \n bbbbbbb \naaaaaaaaa'
    assert result == expected


def test_watch_pyramid_from_the_side_0_2():
    """Returns empty string on empty string."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('') == ''


def test_watch_pyramid_from_above_0_0():
    """Three digit string."""
    from string_pyramid import watch_pyramid_from_above
    result = watch_pyramid_from_above('abc')
    expected = 'aaaaa\nabbba\nabcba\nabbba\naaaaa'
    assert result == expected


def test_watch_pyramid_from_above_0_1():
    """Five digit string."""
    from string_pyramid import watch_pyramid_from_above
    result = watch_pyramid_from_above('abcde')
    expected = 'aaaaaaaaa\nabbbbbbba\nabcccccba\nabcdddcba\nabcdedcba'
    expected += '\nabcdddcba\nabcccccba\nabbbbbbba\naaaaaaaaa'
    assert result == expected


def test_watch_pyramid_from_above_0_2():
    """Returns empty string on empty string."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above('') == ''


def test_count_visible_characters_of_the_pyramid_0_0():
    """Count of three digit string."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('abc') == 25


def test_count_visible_characters_of_the_pyramid_0_1():
    """Count on five digit string."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('abcde') == 81


def test_count_visible_characters_of_the_pyramid_0_2():
    """Return -1 on empty string."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('') == -1


def test_count_all_characters_of_the_pyramid_0_0():
    """Full count of 3 digit string pyramid."""
    from string_pyramid import count_all_characters_of_the_pyramid
    count_all_characters_of_the_pyramid('abc') == 35


def test_count_all_characters_of_the_pyramid_0_1():
    """Count all blocks of 5 digit string pyrimid."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('abcde') == 165
    pass


def test_count_all_characters_of_the_pyramid_0_2():
    """Return -1 on empty string."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('') == -1


# =========================Code Wars Test below ======================== #
# Modified to work with pytest


def visualisation(expected_watch_from_side, expected_watch_from_above,
                  actual_watch_from_side, actual_watch_from_above):
    print('From side correct:\n{}'.format(expected_watch_from_side))
    print('--------------------------------------')
    print('From above correct:\n{}'.format(expected_watch_from_above))
    print('--------------------------------------')
    print('From side yours:\n{}'.format(actual_watch_from_side))
    print('--------------------------------------')
    print('From above yours:\n{}'.format(actual_watch_from_above))
    assert actual_watch_from_side == expected_watch_from_side
    assert actual_watch_from_above == expected_watch_from_above


def test_code_wars_test():
    '''Basic Tests.'''

    '''Handle 2 characters'''
    from string_pyramid import watch_pyramid_from_the_side
    from string_pyramid import watch_pyramid_from_above
    from string_pyramid import count_visible_characters_of_the_pyramid
    from string_pyramid import count_all_characters_of_the_pyramid

    characters = '*#'
    expected_watch_from_side = ' # \n***'
    expected_watch_from_above = '***\n*#*\n***'
    actual_watch_from_side = watch_pyramid_from_the_side(characters)
    actual_watch_from_above = watch_pyramid_from_above(characters)
    visualisation(
        expected_watch_from_side, expected_watch_from_above,
        actual_watch_from_side, actual_watch_from_above
    )
    assert count_visible_characters_of_the_pyramid(characters) == 9
    assert count_all_characters_of_the_pyramid(characters) == 10

    '''should handle 3 characters'''
    characters = 'abc'
    expected_watch_from_side = '  c  \n bbb \naaaaa'
    expected_watch_from_above = 'aaaaa\nabbba\nabcba\nabbba\naaaaa'
    actual_watch_from_side = watch_pyramid_from_the_side(characters)
    actual_watch_from_above = watch_pyramid_from_above(characters)
    visualisation(
        expected_watch_from_side, expected_watch_from_above,
        actual_watch_from_side, actual_watch_from_above
    )
    assert count_visible_characters_of_the_pyramid(characters) == 25
    assert count_all_characters_of_the_pyramid(characters) == 35
