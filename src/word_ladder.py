"""Leetcode 126. Word Ladder II."""


class Solution(object):
    """Solution object."""

    def findLadders(self, beginWord, endWord, wordList):
        """Find shortest paths.

        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        graph = Graph()
        graph.add_node(beginWord)
        for word in wordList:
            graph.add_node(word)
            for node in graph.nodes():
                count = 0
                for i, letter in enumerate(word):
                    if letter is not node[i]:
                        count += 1
                if count == 1:
                    graph.add_edges(word, node)
        paths = graph.find_paths(beginWord, endWord)
        if paths:
            length = min((len(path) for path in paths))
        return [path for path in paths if len(path) == length]


class Graph(dict):
    """Create a graph data strcture modeled off a dictionary."""

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self.keys())

    def add_node(self, val):
        """Add a new node with value 'val' to the graph."""
        if val not in self:
            self.setdefault(val, [])

    def add_edges(self, val1, val2):
        """Add a new edge to the graph."""
        self.setdefault(val1, [])
        self.setdefault(val2, [])
        if val2 not in self[val1]:
            self[val1].append(val2)
        if val1 not in self[val2]:
            self[val2].append(val1)

    def find_paths(self,  start_val, end_val):
        """Find paths."""
        queue = [(start_val, [start_val])]
        while queue:
            (node, path) = queue.pop(0)
            for val in [x for x in self[node] if x not in set(path)]:
                print(path)
                if val == end_val:
                    yield path + [val]
                else:
                    queue.append((val, path + [val]))


find = Solution()
beginWord = "qa"
endWord = "sq"
# wordList = [
#     "qb", "ab", "xb", "ac", "xg"
# ]
wordList = [
    "si", "go", "se", "cm", "mb", "sb", "kr", "ln",
    "tm", "to",
    "fa", "yo", "ho", "ma", "re", "or",
    "rn", "pt", "io",
    "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq"
]
print(find.findLadders(beginWord, endWord, wordList))
