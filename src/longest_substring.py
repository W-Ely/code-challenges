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
            if ord(char) in ref:
                longest = max(ref[ord(char)] - i, longest)
            ref[ord(char)] = i
        return longest
