"""
Monotonic Array:

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.
Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. 
 Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.
Note that empty arrays and arrays of one element are monotonic.

https://leetcode.com/problems/monotonic-array/
"""


# O(n) time | O(1) space - where n is the length of the array
def isMonotonic(array):
    if len(array) < 2:
        return True

    is_increasing = False
    order_determined = False

    prev = array[0]
    idx = 1
    while idx < len(array):

        # determine if increasing or decreasing
        if not order_determined:
            if prev < array[idx]:
                is_increasing = True
                order_determined = True
            elif prev > array[idx]:
                order_determined = True

        # check if isMonotonic
        if is_increasing:
            if array[idx] >= prev:
                prev = array[idx]
                idx += 1
            else:
                print(array[idx])
                return False
        else:
            if array[idx] <= prev:
                prev = array[idx]
                idx += 1
            else:
                return False

    return True


print(isMonotonic([1, 2, 3, 4, 5]))
print(isMonotonic([2, 2, 2, 4, 6, 7]))
print(isMonotonic([-1, -5, 10]))
print(isMonotonic([2, 2, 2, 1, 4, 5]))


def isMonotonic1(array):
    if len(array) < 3:
        return True

    is_increasing = None

    for idx in range(1, len(array)):

        # set is_increasing variable
        if is_increasing is None and array[idx] != array[idx-1]:
            is_increasing = array[idx] > array[idx-1]

        # check for error
        if array[idx-1] > array[idx] and is_increasing == True:
            return False
        if array[idx-1] < array[idx] and is_increasing == False:
            return False

    return True
