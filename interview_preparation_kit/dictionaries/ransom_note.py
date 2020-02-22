"""
Contains the solution to problem 1 of the Dictionaries section.

Problem
-------
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him
through his handwriting. He found a magazine and wants to know if he can cut out entire words from
it and use them to create an untraceable replica of his ransom note. The words in his note are
case-sensitive and he must use only entire words available in the magazine. He cannot use
substrings or concatenation to create the words he needs.

Given the words of length `m` in the `magazine` and the words of length `n` needed in the ransom
`note`, return `Yes` if he can replicate his ransom note exactly using the entire words from the
magazine; otherwise, return `No`.

For example,
    the note is "Attack at dawn". The magazine contains only "attack at dawn".
    The magazine has all the right words, but there's a case mismatch.
    Thus the answer is `No`.

Write a function to return `Yes` or `No` based on the above condition.

Constraints
-----------
*   1 <= m, n <= 30000
*   1 <= |magazine[i]|, |note[i]| <= 5
*   Each word consists of English alphabetic letters (i.e., `a` to `z` and `A` to `Z`)

"""

from collections import Counter


def check_magazine(magazine, note):  # T(n), S(m)
    """Return `Yes` if the note can be formed using the magazine, else `No`."""
    # check if the length of note is greater than magazine
    if len(note) > len(magazine):
        return 'No'

    magazine_dict = Counter(magazine)  # S(m)
    for word in note:  # T(n)
        # if the word does not exists (None) and if the count of the word is zero (0)
        if not magazine_dict.get(word):
            return 'No'
        magazine_dict[word] -= 1

    return 'Yes'
