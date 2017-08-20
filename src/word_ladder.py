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
        shortest = False
        stack = [(beginWord, [beginWord])]
        paths = []
        word_length = len(beginWord)
        while not shortest and stack:
            temp = []
            while stack:
                word, path = stack.pop()
                wordList.discard(word)
                for i in range(word_length):
                    for char in chars:
                        new_word = word[:i] + char + word[i + 1:]
                        if new_word in wordList:
                            if new_word == endWord:
                                shortest = True
                                paths.append(path + [new_word])
                            else:
                                temp.append(
                                    (new_word,  path + [new_word])
                                )
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
# print(find.findLadders(beginWord, endWord, wordList))
# import timeit
# print(timeit.timeit('test = {"test"}; test2 = "test"; test2 in test', number=10000))
