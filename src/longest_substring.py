"""Leetcode 3. Longest Substring Without Repeating Characters."""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ref = {}
        chars = set()
        longest = 0
        j = 0
        temp = {}
        for i, char in enumerate(s):
            while j < len(s) and s[j] not in chars:
                ref[s[j]] = {}
                ref[s[j]]["start"] = j
                ref[char]["end"] = j
                longest = max(ref[char]["end"]- ref[char]["start"] + 1, longest)
                chars.add(s[j])
                j += 1
            del ref[char]
            chars.remove(char)
        return longest
