"""Tests for the interview_preparation_kit.array.hourglass module."""

from hypothesis import given
from hypothesis.strategies import integers, lists

from interview_preparation_kit.arrays.hourglass import hourglass_sum


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
def test_hourglass_sum(array):
    """hourglass_sum() should return the maximum hourglass sum for the given input array."""
    max_sum = hourglass_sum(array)

    assert -63 <= max_sum <= 63
