"""
Contains the solution to problem 4 of the warm up section.

Problem
-------
Lilah has a string `s` of lowercase English letters that she repeated infinitely many times.

Given an integer `n`, find the number of letter a's (lowercase) in the first `n` letters of Lilah's
infinite string.

For example,
    if the string 'abcac' and n = 10, the substring we consider is 'abcacabcac', the first
    10 characters of her infinite string. There are 4 occurrences of `a` in the substring.

Write a function which returns the number of occurrences of `a` in the infinitely repeating
string (prefix) of length `n`.

Constraints
-----------
*   1 <= s <= 100
*   1 <= n <= 10 ** 12

"""


# `n` in complexity denotes the length of `string`
def number_of_occurrence_of_a(string, infinite_string_length):  # T(n), S(1)
    """Return the number of occurrences of `a` in the infinitely repeating string."""
    substring = 'a'
    # if infinite string length is less than the length of the string
    if infinite_string_length <= len(string):  # T(n)
        return string.count(substring, 0, infinite_string_length)

    base_count = string.count(substring)  # T(n)
    num_repetitions = infinite_string_length // len(string)
    rem_string_len = infinite_string_length % len(string)

    total_count = base_count * num_repetitions + string.count(substring, 0, rem_string_len)  # T(n)

    return total_count
