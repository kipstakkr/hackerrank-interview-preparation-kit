"""
Contains the solution to problem 2 of the warm up section.

Problem
-------
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details
like topography. During his last hike he took exactly `n` steps. For every step he took, he noted
if it was an uphill `U`, or a downhill `D` step. Gary's hikes start and end at sea level and each
step up or down represents a `1` unit change in altitude.

We define the following terms:
*   A mountain is a sequence of consecutive steps above sea level, starting with a step up from
    sea level and ending with a step down to sea level.
*   A valley is a sequence of consecutive steps below sea level, starting with a step down from
    sea level and ending with a step up to sea level.

Given Gary's sequence of up and down steps during his last hike, find the number of valleys he
walked through.

For example,
    if Gary's path (represented as a string `s`) `DDUUUUDD`, he first enters a valley `2` units
    deep. Then he climbs out and up onto a mountain `2` units high. Finally, he returns to sea
    level and ends his hike.

Write a function to return an integer representing the number of valleys Gary walked through from
the given step sequence.

Constraints
-----------
*   2 <= n <= 10 ** 6
*   s[i] = {'U', 'D'}
*   0 <= i < n

"""


def number_of_valleys(string):  # T(n), S(1)
    """Return the number of valleys present in the given string representing step sequence."""
    valleys, step_units = 0, 0
    up, down = 'U', 'D'
    for step in string:  # T(n)
        if step == up:
            step_units += 1
            if not step_units:
                valleys += 1
        elif step == down:
            step_units -= 1

    return valleys
