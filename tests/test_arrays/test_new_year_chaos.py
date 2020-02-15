"""Tests for the interview_preparation_kit.array.new_year_chaos module."""

from interview_preparation_kit.arrays.new_year_chaos import get_min_bribes

import pytest


@pytest.mark.parametrize(
    'mock_queue, expected_result',
    [
        ([2, 1, 5, 3, 4], 3),
        ([2, 5, 1, 3, 4], 'Too chaotic'),
        ([5, 1, 2, 3, 7, 8, 6, 4], 'Too chaotic'),
        ([1, 2, 5, 3, 7, 8, 6, 4], 7)
    ]
)
def test_get_min_bribes(mock_queue, expected_result):
    """get_min_bribes() should return the minimum bribes that took place in the given queue."""
    assert get_min_bribes(mock_queue) == expected_result
