"""Module tests Autocomplete."""
from autocomplete import Autocomplete

#
# def test_autocomplete_with_simple_list_of_words():
#     """Test returns all five words."""
#     vocab = ['test', 'testt', 'tesst', 'testing', 'tested']
#     auto = Autocomplete(vocab)
#     for word in vocab:
#         assert word in auto('tes')
#
#
# def test_autocomplete_with_simple_list_of_words_is_five_long():
#     """Test returns length five."""
#     vocab = ['test', 'testt', 'tesst', 'testing', 'tested']
#     auto = Autocomplete(vocab)
#     assert len(auto('tes')) == 5


# def test_autocomplete_words_file():
#     """Test vocab from file."""
#     vocab = './src/STATIC/words'
#     auto = Autocomplete(vocab)
#     assert len(auto('a')) == 5


def test_autocomplete_none_found_retruns_empty_list():
    """Test return empty list is no word found."""
    auto = Autocomplete(
        ['test', 'testt', 'tesst', 'testing', 'tested']
    )
    assert auto('xyzzy') == []
