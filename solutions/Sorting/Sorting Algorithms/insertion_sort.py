"""
Insertion Sort:
"""


# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def insertionSort(array):

    for idx in range(len(array)-1):

        nxt = idx + 1
        curr = idx
        # comparisons (like bubble sort)
        while curr >= 0 and array[curr] > array[nxt]:

            array[curr], array[nxt] = array[nxt], array[curr]  # swap

            curr -= 1
            nxt -= 1

    return array


"""
Divide the input array into two subarrays in place. 
The first subarray should be sorted at all times and should start with a length of 1, while the second subarray should be unsorted. 
Iterate through the unsorted subarray, inserting all of its elements into the sorted subarray in the correct position by swapping them into place.
Eventually, the entire array will be sorted.
"""


def insertionSort00(array):

    for i in range(1, len(array)):

        # # add a new element(array[i]) to the `sorted array`
        # the sorted array will now end at i
        added = i
        while added > 0 and array[added] < array[added-1]:
            # swap
            array[added], array[added-1] = array[added-1], array[added]
            added -= 1

    return array


"""
- Start with a 'sorted array' of size one at index 0

- add the element to the right of the sorted array to the `sorted array` and
	swap it with other elements till it reaches a balanced position
- repeat the steps above till you reach the end of the array
"""
