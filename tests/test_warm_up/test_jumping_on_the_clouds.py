"""Tests for the interview_preparation_kit.warm_up.jumping_on_the_clouds module."""

from interview_preparation_kit.warm_up.jumping_on_the_clouds import number_of_jumps

import pytest


@pytest.mark.parametrize(
    'mock_clouds, expected_result',
    [
        ([0, 1, 0, 0, 0, 1, 0], 3),
        ([0, 0, 1, 0, 0, 1, 0], 4),
        ([0, 0, 0, 0, 1, 0], 3),
        ([0, 0], 1),
        ([0, 1, 0], 1),
        ([0] * 100, 50)
    ]
)
def test_number_of_jumps(mock_clouds, expected_result):
    """number_of_jumps() should return minimum number of jumps on the clouds to win the game."""
    assert number_of_jumps(mock_clouds) == expected_result
