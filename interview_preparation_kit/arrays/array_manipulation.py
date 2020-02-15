"""
Contains the solution to problem 5 of the array section.

Problem
-------
Starting with a 1-indexed array of zeros and a list of `m` queries, for each operation add a value
`k` to each of the array element between two given indices `a` and `b`, inclusive. Once all queries
have been performed, return the maximum value in your array.

For example,
    For a length `n` (=10) of your array of zeros and a list of queries as follows:
        a b k
        - - -
        1 5 3
        4 8 7
        6 9 1
    Add the values of `k` between the indices `a` and `b` inclusive, and return the largest value
    from the resultant array (after performing all the above queries), which is `10` for example.

Write a function which returns an integer denoting the maximum value in the resultant array.

Constraints
-----------
*   3 <= n <= 10 ** 7
*   1 <= m <= 2 * 10 ** 5
*   1 <= a <= b <= n
*   0 <= k <= 10 ** 9

"""


def manipulate_array(length, queries):  # T(n), S(n)
    """Return the maximum value of the array of `length` after performing all the `queries`."""
    # create the array of zeros of length `length + 1`
    array = [0] * (length + 1)  # S(n)

    for query in queries:  # T(n)
        start_index, end_index, value = query[0] - 1, query[1], query[2]

        # increment and decrement the `value` at the start and end index respectively,
        # for getting the value at a given index while performing the running sum operation,
        # which in turn helps to find the max value
        array[start_index] += value
        array[end_index] -= value

    max_value, running_sum = 0, 0
    for element in array:  # T(n)
        running_sum += element
        if running_sum > max_value:
            max_value = running_sum

    return max_value
