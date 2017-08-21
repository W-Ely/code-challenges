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
        chars = [char for char in 'abcdefghijklmnopqrstuvwxyz']
        stack = [[beginWord]]
        paths = []
        while not paths and stack:
            temp = []
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
            stack = temp
        return paths
#
# #
# find = Solution()
# beginWord = "red"
# endWord = "tax"
# wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
# beginWord = "qa"
# endWord = "sq"
# wordList = [
#     "si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln",
#     "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra",
#     "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
#     "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb",
#     "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz",
#     "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo",
#     "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io",
#     "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"
# ]
# # print(find.findLadders(beginWord, endWord, wordList))
# import timeit
# print(timeit.timeit('test = []; test.append("test")', number=10000))
# print(timeit.timeit('test = []; test += ["test"]', number=10000))
