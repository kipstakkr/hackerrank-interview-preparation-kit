"""Tests for the interview_preparation_kit.dictionaries.sherlock_and_anagrams module."""

from interview_preparation_kit.dictionaries.sherlock_and_anagrams import (
    count_anagram_substring_pairs
)

import pytest


@pytest.mark.parametrize(
    'mock_string, expected_result',
    [
        ('abba', 4),
        ('abcd', 0),
        ('ifailuhkqq', 3),
        ('kkkk', 10),
        ('cdcd', 5)
    ]
)
def test_count_anagram_substring_pairs(mock_string, expected_result):
    """count_anagram_substring_pairs() should return the count of pairs of anagram substrings."""
    assert count_anagram_substring_pairs(mock_string) == expected_result
