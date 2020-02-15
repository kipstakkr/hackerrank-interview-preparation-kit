"""
Contains the solution to problem 3 of the array section.

Problem
-------
Whenever a new movie of a popular actor/actress is yet to release in cinemas, fans would like to
watch the FDFS of the movie along with family/friends. But there is no online portal to book
tickets in the city, and thus they have to physically go to the cinemas to book tickets.
In this city, people like to follow queue system. But even with this, some people would like to
make use of this opportunity to earn quick bucks/bribes.

Each person wears a sticker indicating their initial position in the queue. Initial positions
increment by `1` from `1` at the front of the line to `n` at the back. Any person in the queue
can bribe the person directly in front of them to swap positions. If two people swap positions,
they still wear the same sticker denoting their original places in line. One person can bribe
at most two others.

For example,
    if n = 8 and Person 5 bribed Person 4, then the queue will look like:
        1, 2, 3, 5, 4, 6, 7, 8

Write a function to return an integer representing the minimum number of bribes that took place to
get the queue to its current state, or return 'Too chaotic' if current state queue is not possible.

Constraints
-----------
*   1 <= n <= 10 ** 5

"""


def get_min_bribes(queue):  # T(n), S(1)
    """Return the minimum number of bribes that took place in the given queue."""
    bribes = 0

    # initialize the variables to keep track of the people bribed by the current person.
    # apart from the initialization, `person_1` will always be strictly less than `person_2`
    # using these two variables, we will get to know the number of people bribed by a person,
    # based on the persons' sticker:

    # 1. If current person < person_1, the current person hasn't bribed anyone
    # 2. If person_1 < current_person < person_2, the current person has bribed 1 person
    # 3. If current_person > person_2, the current person has bribed 2 persons
    person_1, person_2 = (float('Inf'),) * 2

    # loop through the queue in reverse order
    for index in reversed(range(len(queue))):  # T(n)

        # 'too chaotic'
        if queue[index] - (index + 1) > 2:
            return 'Too chaotic'

        # bribed 2 persons
        elif queue[index] > person_2:
            bribes += 2

        # bribed 1 person
        elif queue[index] > person_1:
            bribes += 1
            person_2 = queue[index]

        # bribed no one
        else:
            person_1, person_2 = queue[index], person_1

    return bribes
