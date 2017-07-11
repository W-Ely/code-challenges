"""Module implements an Autocomplete class."""
from trie import Trie


class Autocomplete(Trie):
    """Implement Autocomplete using a trie."""

    def __init__(self, words, max_completions=5):
        """Init the Autocomplete."""
        Trie.__init__(self)
        self._comps = max_completions
        try:
            with open(words, 'r') as file:
                for line in file:
                    self.insert(" ".join(line.split()))
        except Exception:
            for word in words:
                self.insert(word)

    def __call__(self, string):
        """Call class, get a list."""
        auto = self.word_traverse(string)
        return [next(auto) for _ in range(self._comps)]
