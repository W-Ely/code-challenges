"""Trapping rain water."""


class Solution(object):
    """Trap water."""

    def trap(self, heights):
        """Trap some rain water.

        :type heights: List[int]
        :rtype: int
        """
        water = 0
        if heights:
            left = [0 for _ in range(len(heights))]
            right = left[:]

            left[0] = heights[0]
            for i in range(1, len(heights)):
                left[i] = max(left[i-1], heights[i])

            right[-1] = heights[-1]
            for i in range(len(heights) - 2, -1, -1):
                right[i] = max(right[i+1], heights[i])

            for i in range(len(heights)):
                water += min(left[i], right[i]) - heights[i]

        return water
