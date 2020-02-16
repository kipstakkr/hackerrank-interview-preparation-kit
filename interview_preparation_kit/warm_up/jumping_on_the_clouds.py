"""
Contains the solution to problem 2 of the warm up section.

Problem
-------
Emma is playing a new mobile game that starts with consecutively numbered clouds `c`. Some of the
clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number
that is equal to the number of the current cloud plus `1` or `2`. She must avoid the thunderheads.

Determine the minimum number of jumps it will take Emma to jump from her starting position to the
last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered `0` if they are safe or `1` if they must
be avoided.

Write a function to return the minimum number of jumps required to win the game.

Constraints
-----------
*   2 <= n <= 100
*   c[i] = {0, 1}
*   c[0] = c[n - 1] = 0

"""


def number_of_jumps(clouds):
    """Return the minimum number of jumps to make in the given clouds list to win the game."""
    num_jumps = 0
    jump_index = 0
    while jump_index + 1 < len(clouds):
        if jump_index + 2 < len(clouds) and not clouds[jump_index + 2]:
            jump_index += 2
        else:
            jump_index += 1

        num_jumps += 1

    return num_jumps
