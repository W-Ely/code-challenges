"""Leetcode 1. Two Sum."""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ref = {}
        for i, num in enumerate(nums):
            possible = target - num
            if possible in ref:
                return [ref[possible], i]
            ref[num] = i
