"""Tests for the interview_preparation_kit.warm_up.sock_merchant module."""

from interview_preparation_kit.warm_up.sock_merchant import number_of_sock_pairs

import pytest


@pytest.mark.parametrize(
    'mock_array, expected_result',
    [
        ([1, 2, 1, 2, 1, 3, 2], 2),
        ([10, 20, 20, 10, 10, 30, 50, 10, 20], 3),
        ([1, 1, 3, 1, 2, 1, 3, 3, 3, 3], 4),
        ([20], 0),
        ([10] * 100, 50)
    ]
)
def test_number_of_sock_pairs(mock_array, expected_result):
    """number_of_sock_pairs() should return the number of sock pairs of matching colors."""
    assert number_of_sock_pairs(mock_array) == expected_result
