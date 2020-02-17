"""Tests for the interview_preparation_kit.dictionaries_and_hashmaps.ransom_note module."""

from interview_preparation_kit.dictionaries_and_hashmaps.ransom_note import check_magazine

import pytest


@pytest.mark.parametrize(
    'mock_magazine, mock_note, expected_result',
    [
        (
            ['give', 'me', 'one', 'grand', 'today', 'night'],
            ['give', 'one', 'grand', 'today'],
            'Yes'
        ),
        (
            ['two', 'times', 'three', 'is', 'not', 'four'],
            ['two', 'times', 'two', 'is', 'four'],
            'No'
        ),
        (
            ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts'],
            ['ive', 'got', 'some', 'coconuts'],
            'No'
        ),
        (
            ['Goku', 'is', 'the', 'strongest', 'of', 'all', 'saiyans'],
            ['goku', 'is', 'the', 'strongest', 'of', 'all', 'saiyans'],
            'No'
        ),
        (
            ['wait', 'a', 'minute', 'is', 'that', 'place', 'the', 'sun'],
            ['is', 'that', 'place', 'the', 'sun'],
            'Yes'
        )
    ]
)
def test_check_magazine(mock_magazine, mock_note, expected_result):
    """check_magazine() should check whether the note can be made from the given magazine."""
    assert check_magazine(mock_magazine, mock_note) == expected_result
