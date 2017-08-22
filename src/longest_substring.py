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
            else:
                ref[ord(char)] = i
                longest = max(ref[ord(char)] , longest)
            ref[ord(char)] = i
        return longest

find = Solution()
string = "abcbed"
print(find.lengthOfLongestSubstring(string))
