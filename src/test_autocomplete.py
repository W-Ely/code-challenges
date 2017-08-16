"""Module tests Autocomplete."""
from autocomplete import Autocomplete
import pytest


def test_autocomplete_with_simple_list_of_words():
    """Test returns all five words."""
    vocab = ['test', 'testt', 'tesst', 'testing', 'tested']
    auto = Autocomplete(vocab)
    for word in vocab:
        assert word in auto('tes')


def test_autocomplete_with_simple_list_of_words_is_five_long():
    """Test returns length five."""
    vocab = ['test', 'testt', 'tesst', 'testing', 'tested']
    auto = Autocomplete(vocab)
    assert len(auto('tes')) == 5


def test_autocomplete_words_file():
    """Test vocab from file."""
    vocab = './src/STATIC/words'
    auto = Autocomplete(vocab)
    assert len(auto('a')) == 5


def test_autocomplete_none_found_retruns_empty_list():
    """Test return empty list is no word found."""
    auto = Autocomplete(
        ['test', 'testt', 'tesst', 'testing', 'tested']
    )
    assert auto('xyzzy') == []


def test_autocomplete_with_only_three_found_words():
    """Test autocomplete returns the only three found."""
    auto = Autocomplete(
        ['test', 'xyzzy', 'tesst', 'testing', 'tested']
    )
    assert len(auto('test')) == 3


def test_handles_non_list_instantiation():
    """Test Autocomplete requires a list."""
    with pytest.raises(TypeError):
        Autocomplete('test')


def test_handles_non_string_call_param():
    """Test handles non string call param."""
    auto = Autocomplete(
        ['test', 'xyzzy', 'tesst', 'testing', 'tested']
    )
    assert auto({'test': 'test'}) == []


def test_handles_non_numeric_max_completions_input():
    """Test non numeric max_completion."""
    with pytest.raises(TypeError):
        Autocomplete(['test'], 'Not a Number')
