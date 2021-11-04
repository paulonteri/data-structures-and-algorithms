"""
Move Element To End:

You're given an array of integers and an integer.
Write a function that moves all instances of that integer in the array to the end of the array and returns the array.
The function should perform this in place (i.e., it should mutate the input array) 
 and doesn't need to maintain the order of the other integers.
"""


# O(n) time | O(1) space - where n is the length of the array
def moveElementToEnd(array, toMove):

    pos = 0
    next_swap = 0

    # move all non-toMove nums to the front (skip toMove(s))
    while pos < len(array):
        if array[pos] != toMove:
            # swap
            array[pos], array[next_swap] = array[next_swap], array[pos]

            next_swap += 1
            pos += 1
        else:
            pos += 1

    return array


def moveElementToEnd2(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right:
        if array[right] == toMove:
            # the element at array[right] is at its correct place so we skip it
            right -= 1
        elif array[left] == toMove:  # (and array[right] != toMove)
            # swap
            array[right], array[left] = array[left], array[right]

            right -= 1
            left += 1
        else:  # array[right] != toMove & array[left] != toMove
            left += 1
        return array
