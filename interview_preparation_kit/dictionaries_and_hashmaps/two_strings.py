"""
Contains the solution to problem 2 of the Dictionaries and Hashmaps section.

Problem
-------
Given two strings `s1` and `s2`, determine if they share a common substring. A substring may be as
small as one character.

Write a function to return a string, either `YES` or `NO` based on whether the strings share a
common substring.

Constraints
-----------
* 1 <= |s1|, |s2| <= 10 ** 5
* s1[i], s2[j] = ascii[a-z] (lowercase alphabets)
* 0 <= i < |s1|
* 0 <= j < |s2|

"""


def check_common_substring(string_1, string_2):  # T(m + n), S(1)
    """Return either `YES` or `NO` based on whether the strings share a common substring or not."""
    string_set_1 = set(string_1)  # T(m), S(26)
    string_set_2 = set(string_2)  # T(n), S(26)

    if string_set_1.isdisjoint(string_set_2):  # T(26)
        return 'NO'
    else:
        return 'YES'
