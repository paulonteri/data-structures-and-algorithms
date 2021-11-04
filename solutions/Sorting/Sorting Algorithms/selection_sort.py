"""
Selection Sort
"""


# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selectionSort(array):

    pos_to_insert = 0
    while pos_to_insert < len(array):
        smallest = pos_to_insert

        # find smallest
        for idx in range(pos_to_insert+1, len(array)):
            if array[idx] < array[smallest]:
                smallest = idx

        # swap
        array[pos_to_insert], array[smallest] = array[smallest], array[pos_to_insert]

        pos_to_insert += 1

    return array


"""
Divide the input array into two subarrays in place. 
The first subarray should be sorted at all times and should start with a length of 0, while the second subarray should be unsorted.
Find the smallest (or largest) element in the unsorted subarray and insert it into the sorted subarray with a swap.
Repeat this process of finding the smallest (or largest) element in the unsorted subarray and
 inserting it in its correct position in the sorted subarray with a swap until the entire array is sorted.
"""

# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space


def selectionSort00(array):

    # select the smallest element and place it at i
    for i in range(len(array)-1):

        smallest = i
        for idx in range(i+1, len(array)):
            if array[smallest] > array[idx]:
                smallest = idx

        # swap
        array[i], array[smallest] = array[smallest], array[i]

    return array
