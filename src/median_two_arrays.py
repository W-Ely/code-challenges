"""Leetcode 4. Median of Two Sorted Arrays."""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


    def merge_sort(numbers):
        """Recursively split list and returns merged list."""
        if len(numbers) <= 1:
            return numbers
        middle_idx = int(len(numbers) / 2)
        left = merge_sort(numbers[:middle_idx])
        right = merge_sort(numbers[middle_idx:])
        results = []
        i, j = 0, 0
        while len(results) < len(left) + len(right):
            if left[i] < right[j]:
                results += [left[i]]
                i += 1
            else:
                results += [right[j]]
                j += 1
            if i == len(left) or j == len(right):
                results += left[i:] or right[j:]
                return results
            return merge(left, right)
