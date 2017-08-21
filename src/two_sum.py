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
            posible = target - num
            if posible in ref:
                return [ref[posible], i]
            ref[num] = i
