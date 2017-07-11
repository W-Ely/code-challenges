"""Module tests Autocomplete."""
from autocomplete import Autocomplete


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
