"""
Contains the solution to problem 2 of the array section.

Problem
-------
A left rotation operation on an array shifts each of the array elements 1 unit to the left.
Given an array `a` of `n` integers and a number `d`, perform `d` left rotations on the array.

Write a function to return the resultant array after `d` left shifts.

Constraints
-----------
*   1 <= n <= 10 ** 5
*   1 <= d <= n
*   1 <= a[i] <= 10 ** 6

"""


def rotate_left(array, shift):  # T(n), S(1)
    """Return the resultant array after performing `shift` left shifts on the given array."""
    return array[shift:] + array[:shift]
