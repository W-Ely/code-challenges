"""Module tests rain_water."""
from rain_water import Solution


def test_rain_water_returns_correct_number_with_peak_in_center():
    """Test with peak in center."""
    find = Solution()
    assert find.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
