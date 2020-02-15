"""Tests for the interview_preparation_kit.arrays.minimum_swaps module."""

from interview_preparation_kit.arrays.minimum_swaps import get_min_swaps

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([7, 1, 3, 2, 4, 5, 6], 5),
        ([4, 3, 1, 2], 3),
        ([2, 3, 4, 1, 5], 3),
        ([1, 3, 5, 2, 4, 6, 7], 3)
    ]
)
def test_get_min_swaps(mock_array, expected_result):
    """get_min_swaps() should return the minimum swaps required to make the array sorted."""
    assert get_min_swaps(mock_array) == expected_result
