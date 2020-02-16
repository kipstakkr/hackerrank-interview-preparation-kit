"""Tests for the interview_preparation_kit.warm_up.counting_valleys module."""

from interview_preparation_kit.warm_up.counting_valleys import number_of_valleys

import pytest


@pytest.mark.parametrize(
    'mock_string, expected_result',
    [
        ('DDUUUUDD', 1),
        ('UDDDUDUU', 1),
        ('DDUUDDUDUUUD', 2),
        ('DU', 1),
        ('UD', 0)
    ]
)
def test_number_of_valleys(mock_string, expected_result):
    """number_of_valleys() should return the number of valleys present in the step sequence."""
    assert number_of_valleys(mock_string) == expected_result
