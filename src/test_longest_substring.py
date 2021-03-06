"""Module Tests Leet code 3. Longest Substring Without Repeating Characters."""
from longest_substring import Solution

def test_abcabcbb_substring_abc_len_of_3():
    """Test abcabcbb_is_abc."""
    find = Solution()
    assert find.lengthOfLongestSubstring("abcabcbb") == 3


def test_bbbbbb_substring_b_len_of_1():
    """Test bbbbbbis b and 1."""
    find = Solution()
    assert find.lengthOfLongestSubstring("bbbbbb") == 1


def test_pwwkew_substring_wke_len_of_3():
    """Test pwwkew is wke and 3."""
    find = Solution()
    assert find.lengthOfLongestSubstring("pwwkew") == 3


def test_no_repeats_abcdefg_is_7():
    """Test returns 7."""
    find = Solution()
    assert find.lengthOfLongestSubstring("abcdefg") == 7


def test_random():
    """Test another string."""
    find = Solution()
    assert find.lengthOfLongestSubstring("abcdcbb") == 4


def test_odd_chars():
    """Test odd chars."""
    find = Solution()
    assert find.lengthOfLongestSubstring("-,/Z{{a0") == 5


def test_very_long_string():
    """Test returns 26."""
    find = Solution()
    string = "aaaaaaaaaabbbbbbbbbbbbccccccccccccddddddddd" * 2
    longest = "abcdefghijklmnopqrstuvwxyz"
    test = string + longest + string
    assert find.lengthOfLongestSubstring(test) == 26


def test_all_repeat():
    """Test returns 2."""
    find = Solution()
    assert find.lengthOfLongestSubstring("aaabbb") == 2


def test_empty_string_0():
    """Test empty string returns 0."""
    find = Solution()
    assert find.lengthOfLongestSubstring("") == 0


def test_very_long_one_from_leetcode():
    """Test long one."""
    find = Solution()
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ " * 1000
    string += "abcdefghijklmnopqrstuvwxyzABCD"
    assert find.lengthOfLongestSubstring(string) == 95
