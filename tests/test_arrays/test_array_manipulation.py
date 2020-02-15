"""Tests for the interview_preparation_kit.arrays.array_manipulation module."""

from interview_preparation_kit.arrays.array_manipulation import manipulate_array

import pytest


@pytest.mark.parametrize(
    'mock_length, mock_queries, expected_result',
    [
        (10, [(1, 5, 3), (4, 8, 7), (6, 9, 1)], 10),
        (5, [(1, 2, 100), (2, 5, 100), (3, 4, 100)], 200),
        (10, [(2, 6, 8), (3, 5, 7), (1, 8, 1), (5, 9, 15)], 31)
    ]
)
def test_manipulate_array(mock_length, mock_queries, expected_result):
    """manipulate_array() should return the maximum value after performing the given queries."""
    assert manipulate_array(mock_length, mock_queries) == expected_result
