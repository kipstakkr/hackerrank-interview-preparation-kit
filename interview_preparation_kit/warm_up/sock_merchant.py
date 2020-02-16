"""
Contains the solution to problem 1 of the warm up section.

Problem
-------
John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array `a` of `n` integers representing the color of each sock, determine how many pairs
of socks with matching colors there are.

Write a function to return the number of pairs of socks present in the array with matching colors.

Constraints
-----------
*   1 <= n <= 100
*   1 <= a[i] <= 100
*   0 <= i < n

"""

from collections import defaultdict


def number_of_sock_pairs(array):  # T(n), S(n)
    """Return the number of pairs of socks of matching colors from the given array."""
    # if the length of the array is 1, then there is no sock pair possible
    if len(array) == 1:
        return 0

    # use dictionary to store the frequency of each distinct values in the array
    freq_sock_color = defaultdict(int)  # S(n)
    for sock_color in array:  # T(n)
        freq_sock_color[sock_color] += 1

    # add half of the count (by integer division) to the end result for each sock color
    sock_pairs = 0
    for count in freq_sock_color.values():  # T(n)
        sock_pairs += (count // 2)

    return sock_pairs
