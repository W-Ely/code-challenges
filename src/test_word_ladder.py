"""Test module for word_ladder."""
from word_ladder import Solution


def test_word_ladder_returns_two_paths():
    """Return two paths."""
    find = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ]
    assert find.findLadders(beginWord, endWord, wordList) == expected


def test_no_path_returns_empty_list():
    """Return empty list."""
    find = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["dot", "dog", "lot", "log", "cog"]
    expected = []
    assert find.findLadders(beginWord, endWord, wordList) == expected


def test_single_letter_strings():
    """Single letter strings."""
    find = Solution()
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    expected = [["a", "c"]]
    assert find.findLadders(beginWord, endWord, wordList) == expected


def test_few_more_words():
    """Test a few more."""
    find = Solution()
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    expected = [
        ["red", "ted", "tad", "tax"],
        ["red", "ted", "tex", "tax"],
        ["red", "rex", "tex", "tax"]
    ]
    assert find.findLadders(beginWord, endWord, wordList) == expected


def test_long_one_and_circular():
    """Test circle."""
    find = Solution()
    beginWord = "qa"
    endWord = "sq"
    wordList = [
        "si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln",
        "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra",
        "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
        "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb",
        "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz",
        "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo",
        "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io",
        "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"
    ]
    expected = []
    assert find.findLadders(beginWord, endWord, wordList) == expected
