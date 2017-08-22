"""Leetcode 3. Longest Substring Without Repeating Characters."""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ref = {}
        longest = 0
        for i, char in enumerate(s):
            ref[i] = set()
            to_discard = []
            for key in ref:
                if char in ref[key]:
                    to_discard.append(key)
                else:
                    ref[key].add(char)
                    if len(ref[key]) > longest:
                        longest = len(ref[key])
            for key in to_discard:
                del ref[key]
        return longest
