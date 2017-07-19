"""Module implements an Autocomplete class."""
from trie import Trie


class Autocomplete(Trie):
    """Implement Autocomplete using a trie."""

    def __init__(self, words, max_completions=5):
        """Init the Autocomplete."""
        Trie.__init__(self)
        if type(max_completions) is int and max_completions >= 0:
            self._max_completions = max_completions
        else:
            raise TypeError(
                "Max completions must be a positive integer"
            )
        try:
            with open(words, 'r') as file:
                for line in file:
                    self.insert(" ".join(line.split()))
        except (IOError, TypeError):
            if type(words) in (tuple, list):
                for word in words:
                    self.insert(word)
            else:
                raise TypeError("Please instantiate with list of words.")

    def __call__(self, string):
        """Call class, get a list."""
        auto = self.word_traverse(string)
        result = []
        for _ in range(self._max_completions):
            try:
                result.append(next(auto))
            except (KeyError, StopIteration):
                break
        return result
