""" 
Dutch National Flag Problem:

Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; 
    and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Example 1:
    Input: [1, 0, 2, 1, 0]
    Output: [0 0 1 1 2]
Example 2:
    Input: [2, 2, 0, 1, 2, 0]
    Output: [0 0 1 2 2 2 ]
"""


""" 
- we can have three containers/subarrays in our array for filling in the appropriate number
    - the containers will be marked by the right ending of the 0s and left ending of the right
- we then iterate through the array swapping each number to its appropriate container
"""


def dutch_flag_sort(arr):

    next_zero = 0
    next_two = len(arr)-1
    idx = 0
    while idx < (len(arr)):

        # swap values to their correct place
        if arr[idx] == 0 and idx >= next_zero:
            arr[idx], arr[next_zero] = arr[next_zero], arr[idx]
            next_zero += 1
        elif arr[idx] == 2 and idx <= next_two:
            arr[idx], arr[next_two] = arr[next_two], arr[idx]
            next_two -= 1

        # only leave idx if value is in correct place
        else:
            idx += 1

    return arr


arr = [1, 0, 2, 1, 0]
dutch_flag_sort(arr)
print(arr)


"""
Three Number Sort:

You're given an array of integers and another array of three distinct integers.
The first array is guaranteed to only contain integers that are in the second array, and the second array represents a desired order for the integers in the first array.
For example, a second array of [x, y, z] represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first array.
Write a function that sorts the first array according to the desired order in the second array.
The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use any auxiliary space (i.e., it should run with constant space: O(1) space).
Note that the desired order won't necessarily be ascending or descending and that the first array won't necessarily contain all three integers found in the second array—it might only contain one or two
"""


# divide array into three arrays (in place) and
#  move values order[0] into the first and values order[1] into the third

# O(n) time | O(1) space
def threeNumberSort(array, order):

    first_array_next = 0
    third_array_next = len(array) - 1

    idx = 0
    # while idx < len(array):
    while idx <= third_array_next:

        # add to first array
        if array[idx] == order[0] and idx > first_array_next:
            swap(array, idx, first_array_next)
            first_array_next += 1  # increase first array size

        # add to third array
        elif array[idx] == order[2] and idx < third_array_next:
            swap(array, idx, third_array_next)
            third_array_next -= 1  # increase third array size

        else:
            idx += 1

    return array


def swap(array, idx_one, idx_two):
    array[idx_one], array[idx_two] = array[idx_two], array[idx_one]


# O(n) time | O(1) space - where n is the length of the array
# Bucket sort
def threeNumberSort0(array, order):

    valueCounts = [0, 0, 0]

    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1

    for i in range(3):
        value = order[i]
        count = valueCounts[i]
        numElementsBefore = sum(valueCounts[:i])
        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value
    return array


def threeNumberSort00(array, order):

    # positions to be inserted
    nxt_one = 0
    nxt_three = len(array) - 1

    i = 0
    while i <= nxt_three:

        # remember to compare the i > nxt_one and i < nxt_three to prevent
        #   (example for nxt_one) placing a wrong value (that was at i) within nxt_one's bounds

        if array[i] == order[0] and i > nxt_one:
            array[i], array[nxt_one] = array[nxt_one], array[i]
            nxt_one += 1

        elif array[i] == order[2] and i < nxt_three:
            array[i], array[nxt_three] = array[nxt_three], array[i]
            nxt_three -= 1

        else:
            # only move forward if we are sure we are on the right pl
            i += 1

    return array
