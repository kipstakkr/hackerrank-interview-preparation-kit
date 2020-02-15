"""Tests for the interview_preparation_kit.array.hourglass module."""

from hypothesis import given
from hypothesis.strategies import integers, lists

from interview_preparation_kit.arrays.hourglass import hourglass_sum

import pytest


class TestHourglassSum:
    """hourglass_sum() should return the maximum hourglass sum for the given input array."""

    @pytest.mark.parametrize(
        'mock_array, expected_result',
        [
            (
                [
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 0, 2, 4, 4, 0],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 1, 2, 4, 0]
                ],
                19
            ),
            (
                [
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 9, 2, -4, -4, 0],
                    [0, 0, 0, -2, 0, 0],
                    [0, 0, -1, -2, -4, 0]
                ],
                13
            )
        ]
    )
    def test_hourglass_sum_method_with_custom_values(self, mock_array, expected_result):
        """Tests the accuracy of the method with the expected result."""
        assert hourglass_sum(mock_array) == expected_result

    @given(
        lists(
            lists(
                integers(min_value=-9, max_value=9),
                min_size=6,
                max_size=6
            ),
            min_size=6,
            max_size=6
        )
    )
    def test_hourglass_sum(self, array):
        """Tests the property of the method for the given constraints."""
        max_sum = hourglass_sum(array)

        assert -63 <= max_sum <= 63
