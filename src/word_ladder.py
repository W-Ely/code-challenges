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
        wordList = set(wordList)
        graph =  Graph()
        graph.add_node(beginWord)
        shortest = False
        layer = set(beginWord)
        while not shortest and layer:
            for word in layer:
                wordList.discard(word)
            layer = set()
            for node in graph.nodes():
                for word in wordList:
                    count = 0
                    for i, letter in enumerate(word):
                        if letter is not node[i]:
                            count += 1
                    if count == 1:
                        graph.add_node(word)
                        graph.add_edges(node, word)
                        layer.add(word)
                        if word == endWord:
                            shortest = True
        paths = graph.find_paths(beginWord, endWord)
        return [path for path in paths]


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

    def find_paths(self,  start_val, end_val):
        """Find paths."""
        queue = [(start_val, {start_val}, [start_val])]
        paths = []
        while queue:
            node, ref, path = queue.pop()
            for val in self[node]:
                if val not in ref:
                    if val == end_val:
                        shortest = True
                        paths.append(path + [val])
                    else:
                        queue.append(
                            (val,  ref | set([val]), path + [val])
                        )
        return paths
