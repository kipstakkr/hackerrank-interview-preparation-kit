"""
Contains the solution to problem 1 of the array section.

Problem
-------
Given a 6 x 6 2D array, we define the hourglass to be the subset of values with indices falling
in the given pattern.
    a b c
      d
    e f g
There are 16 hourglasses in the array, and an hourglass sum is the sum of an hourglass' values.

Write a function to return the maximum hourglass sum of the given input array.

Constraints
-----------
*   -9 <= arr[i][j] <= 9
*   0 <= i, j <= 5

"""


def hourglass_sum(array):
    """Return the maximum hourglass sum of the given array."""
    # the row and column length of each hourglass
    hourglass_length = 3

    # number of hourglasses in a row or a column
    num_hourglasses = 4

    max_sum = float('-Inf')
    for row in range(num_hourglasses):
        for column in range(num_hourglasses):

            top = sum(array[row][column: column + hourglass_length])
            mid = array[row + 1][column + 1]
            bottom = sum(array[row + hourglass_length - 1][column: column + hourglass_length])

            total_sum = top + mid + bottom
            if total_sum > max_sum:
                max_sum = total_sum

    return max_sum
