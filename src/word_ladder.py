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
        tree = {beginWord: set()}
        layer = [beginWord]
        chars = 'abcdefghijklmnopqrstuvwxyz'
        shortest = False
        stack = [(beginWord, {beginWord}, [beginWord])]
        paths = []
        while not shortest and layer:
            for word in layer:
                wordList.discard(word)
            temp = []
            for node in layer:
                for i, letter in enumerate(node):
                    for char in chars:
                        word = node[:i] + char + node[i + 1:]
                        if word in wordList:
                            tree[word] = set()
                            tree[node].add(word)
                            temp.append(word)
                            if word is endWord:
                                shortest = True
            layer = temp
        while stack:
            node, ref, path = stack.pop()
            for word in tree[node]:
                if word not in ref:
                    if word == endWord:
                        paths.append(path + [word])
                    else:
                        stack.append(
                            (word,  ref | set([word]), path + [word])
                        )
        return [path for path in paths]
