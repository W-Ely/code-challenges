"""Leetcode 126. Word Ladder II.


After considerable efforts, this one is yet to pass leetcode's tests. It is
still too slow. Perhaps retooling it to alternate between going forward from
the beginWord and then backwards from the endWord would keep the iterations
down a bit, but I've played with this one enough.
"""


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
        chars = [char for char in 'abcdefghijklmnopqrstuvwxyz']
        stack, paths, temp = [[beginWord]], [], []
        while not paths and stack:
            for path in stack:
                wordList.discard(path[-1])
            while stack:
                path = stack.pop()
                for i in range(len(beginWord)):
                    for char in chars:
                        new_word = path[-1][:i] + char + path[-1][i + 1:]
                        if new_word == endWord and new_word in wordList:
                            paths.append(path + [new_word])
                        elif new_word in wordList:
                            temp.append(path + [new_word])
            stack, temp = temp, []
        return paths
