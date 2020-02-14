"""Tests for the interview_preparation_kit.array.left_rotation module."""

from collections import deque

from hypothesis import assume, given, settings
from hypothesis.strategies import integers, lists

from interview_preparation_kit.arrays.left_rotation import rotate_left


@given(lists(integers(min_value=1, max_value=10 ** 6), min_size=1, max_size=10 ** 5),
       integers(min_value=1))
@settings(max_examples=500)
def test_rotate_left(array, shift):
    """rotate_left() should return the given array after performing `shift` left shifts."""
    assume(shift <= len(array))

    temp_array = deque(array).copy()

    # negative for left shifts
    temp_array.rotate(-shift)

    assert rotate_left(array, shift) == list(temp_array)
