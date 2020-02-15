"""
Contains the solution to problem 4 of the array section.

Problem
-------
Given an unordered array `a` consisting of `n` consecutive integers (1, 2, 3, ..., n) without any
duplicates, find the minimum number of swaps required to sort the array in ascending order.
You are allowed to swap any two elements.

Write a function to return the minimum number of swaps required to make the array sorted.

Constraints
-----------
*   1 <= n <= 10 ** 5
*   1 <= a[i] <=n
*   0 <= i < n

"""


def get_min_swaps(array):  # T(n), S(n)
    """Return the minimum number of swaps required to make the array sorted."""
    swaps = 0

    # create a temporary array to store the index of the values to be swapped.
    # thus the temporary array will act as a lookup table and will contain:
    # index => value of the given array
    # value => corresponding index of the given array
    look_up = [0] * (len(array) + 1)  # S(n)
    for index, value in enumerate(array):  # T(n)
        look_up[value] = index

    for index in range(len(array)):  # T(n)
        # as the value start from 1
        position_value = index + 1

        # if the current value is not in its right place
        if array[index] != position_value:
            swap_index = look_up[position_value]
            array[index], array[swap_index] = array[swap_index], array[index]

            # update the lookup table after the swap
            look_up[array[swap_index]] = swap_index

            swaps += 1

    return swaps
