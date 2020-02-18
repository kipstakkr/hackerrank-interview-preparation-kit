"""Tests for the interview_preparation_kit.warm_up.repeated_string module."""

from interview_preparation_kit.warm_up.repeated_string import number_of_occurrence_of_a

import pytest


@pytest.mark.parametrize(
    'mock_string, mock_infinite_string_length, expected_result',
    [
        ('pneumonoultramicroscopicsilicovolcanoconiosis', 40, 2),
        ('aba', 10, 7),
        ('a', 10 ** 11, 10 ** 11),
        ('abcac', 10, 4),
        ('refuse', 10 ** 11, 0)
    ]
)
def test_number_of_occurrence_of_a(mock_string, mock_infinite_string_length, expected_result):
    """number_of_occurrence_of_a() should return the count of `a` in the infinite string."""
    assert number_of_occurrence_of_a(mock_string, mock_infinite_string_length) == expected_result
