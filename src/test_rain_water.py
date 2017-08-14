"""Module tests rain_water."""
from rain_water import Solution


def test_rain_water_returns_correct_number_with_peak_in_center():
    """Test with peak in center."""
    find = Solution()
    assert find.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_rain_water_returns_correct_number_with_big_valley():
    """Test with valley."""
    find = Solution()
    assert find.trap([6, 0, 0, 6]) == 12


def test_rain_water_returns_correct_number_with_double_peak():
    """Test with double peak."""
    find = Solution()
    assert find.trap([0, 3, 0, 0, 3, 0]) == 6


def test_rain_water_returns_correct_number_with_double_valley():
    """Test with double valley."""
    find = Solution()
    assert find.trap([3, 0, 3, 0, 3]) == 6


def test_empty_list():
    """Test with empty list."""
    find = Solution()
    assert find.trap([]) == 0
