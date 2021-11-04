"""
Bubble Sort:
"""


# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubbleSort(array):

    did_swap = False
    while True:
        did_swap = False

        for idx in range(1, len(array)):
            if array[idx] < array[idx-1]:
                # swap
                array[idx],  array[idx-1] = array[idx-1], array[idx]
                did_swap = True

        if not did_swap:
            return array


"""
Traverse the input array, swapping any two numbers that are out of order and keeping track of any swaps that you make.
Once you arrive at the end of the array, check if you have made any swaps;
if not, the array is sorted and you are done; otherwise, repeat the steps laid out in this hint until the array is sorted.
"""


def bubbleSort00(array):
    if len(array) < 2:
        return array

    is_sorted = False
    while not is_sorted:
        is_sorted = True

        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                is_sorted = False
                # swap
                array[i], array[i+1] = array[i+1], array[i]

    return array
