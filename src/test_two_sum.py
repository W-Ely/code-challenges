"""Tests for Leetcode 1 Two Sum."""
from two_sum import Solution


def test_simple_example():
    """Test example."""
    find = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert find.twoSum(nums, target) == expected


def test_same_number():
    """Test same number."""
    find = Solution()
    nums = [2, 7, 7, 15]
    target = 14
    expected = [1, 2]
    assert find.twoSum(nums, target) == expected


def test_very_long():
    """Test a very long list."""
    find = Solution()
    nums = [x for x in range(1, 1000001)]
    target = 1999999
    expected = [999998, 999999]
    assert find.twoSum(nums, target) == expected
