"""
Contains the solution to problem 3 of the Dictionaries section.

Problem
-------
Two strings are anagrams of each other if the letters of one string can be rearranged to form the
other string. Given a string `s`, find the number of pairs of substrings of the string that are
anagrams of each other.

For example,
    if the given string s = `mom`, then the list of all anagrammatic pairs is
    [`m`, `m`], [`mo`, `om`] at positions [[0], [2]], [[0, 1], [1, 2]] respectively.

Write a function to return an integer denoting the number of pairs of substrings of the string that
are anagrams of each other.

Constraints
-----------
*   2 <= |s| <= 100
*   s[i] = ascii[a-z] (lowercase alphabets)
*   0 <= i < |s|

"""
from collections import defaultdict


def count_anagram_substring_pairs(string):  # T(n ** 3), S(n ** 2)
    """Return the count of the number of pairs of anagram substrings from the given string."""
    alphabets = 26
    signature_dict_count = defaultdict(int)  # S(n ** 2)

    for start in range(len(string)):  # T(n)
        for end in range(start, len(string)):  # T(n)
            signature = [0 for _ in range(alphabets)]  # S(26)
            for char in string[start: end + 1]:  # T(n)
                signature[ord(char) - ord('a')] += 1

            signature = tuple(signature)
            signature_dict_count[signature] += 1

    num_anagram_pairs = 0
    for count in signature_dict_count.values():  # T(n ** 2)
        num_anagram_pairs += ((count * (count - 1)) // 2)

    return num_anagram_pairs
