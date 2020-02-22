"""Tests for the interview_preparation_kit.dictionaries.two_strings module."""

from interview_preparation_kit.dictionaries.two_strings import check_common_substring

import pytest


@pytest.mark.parametrize(
    'mock_string_1, mock_string_2, expected_result',
    [
        ('hello', 'world', 'YES'),
        ('hi', 'world', 'NO'),
        ('wouldyoulikefries', 'abcabcabcabcabcabc', 'NO'),
        ('hackerrankcommunity', 'cdecdecdecde', 'YES'),
        ('jackandjill', 'wentupthehill', 'YES'),
        ('writetoyourparents', 'fghmqzldbc', 'NO'),
        ('aardvark', 'apple', 'YES'),
        ('beetroot', 'sandals', 'NO')
    ]
)
def test_check_common_substring(mock_string_1, mock_string_2, expected_result):
    """check_common_substring() should check whether the two strings have a common substring."""
    assert check_common_substring(mock_string_1, mock_string_2) == expected_result
