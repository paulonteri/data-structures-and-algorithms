"""
Single Cycle Check:

You're given an array of integers where each integer represents a jump of its value in the array.
For instance, the integer 2 represents a jump of two indices forward in the array;
    the integer -3 represents a jump of three indices backward in the array.
If a jump spills past the array's bounds, it wraps over to the other side. 
For instance, a jump of -1 at index 0 brings us to the last index in the array. 
Similarly, a jump of 1 at the last index in the array brings us to index 0.

Write a function that returns a boolean representing whether the jumps in the array form a single cycle.
A single cycle occurs if, starting at any index in the array and following the jumps,
    every element in the array is visited exactly once before landing back on the starting index.

Sample Input
    array = [2, 3, 1, -4, -4, 2]
Sample Output
    true


https://www.algoexpert.io/questions/Single%20Cycle%20Check
"""


# 0(n) time | 0(n) space
def hasSingleCycle(array):

    visited = {}  # visited indexes
    idx = 0
    while True:

        # # jump logic (find where we are visiting)
        idx = getNextIdx(idx, array)

        # if we have been at this index before (which will eventually happen):
        if idx in visited:
            # if len(visited) is the same as len(array),
            #   then we must have done one complete loop including every element
            #   will handle cycles that do not cover all elements in the array
            return len(visited) == len(array)

        # # visit index
        visited[idx] = True


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


def hasSingleCycle00(array):
    indices = [0] * len(array)

    i = 0
    for _ in range(len(array)*2):
        # mark current index as visted
        indices[i] = indices[i] + 1

        # move to next index
        i += array[i]
        if i > len(array) - 1:  # too large
            i = i % len(array)
        while i < 0:
            i += len(array)

    # look for invalid
    for num in indices:
        if num != 2:
            return False

    return True


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

after len(array)-1 visits, we should land at index 0
"""


# 0(n) time | 0(1) space
def hasSingleCycle2(array):
    # after len(array)-1 visits, we should land at index 0

    num_elements_visited = 0
    idx = 0
    while num_elements_visited < len(array):
        if num_elements_visited > 0 and idx == 0:
            return False

        num_elements_visited += 1
        idx = getNextIdx(idx, array)

    return idx == 0


def getNextIdx(idx, array):

    # # jump logic (find where we are visiting)
    idx = idx + array[idx]
    while idx >= len(array) or idx < 0:
        if idx >= len(array):
            idx -= len(array)
        if idx < 0:
            idx += len(array)

    return idx


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


def hasSingleCycle0(array):

    counter = 0

    idx = 0
    while counter < len(array):
        if array[idx] == float("-inf"):
            return False

        idx_val = array[idx]
        # mark as visited
        array[idx] = float("-inf")

        # jump
        idx += idx_val
        counter += 1

        while idx < 0:
            idx += len(array)
        while idx > len(array) - 1:
            idx -= len(array)

    return idx == 0


"""

[0, 1, 2,  3,  4, 5]
[2, 1, 1,  1,  1, 1]
[2, 3, 1, -4, -4, 2]



"""
