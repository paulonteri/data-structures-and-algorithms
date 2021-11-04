""" 
Squaring a Sorted Array:

Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
"""


""" 
(arrange from largest to smallest then reverse)
- beacause our input array contains negative numbers, 
    the largest square can be either on the far right or far left
- so we need tto iterate inwards (from outward):
    - have a left & right pointer at both ends of the array and consider the largest square 


Use two pointers starting at both ends of the input array. 
At any step, whichever pointer gives us the bigger square, 
we add it to the result array and move to the next/previous number according to the pointer.
"""


def make_squares(arr):
    squares = []

    left = 0
    right = len(arr)-1
    while left <= right:
        left_s = arr[left] * arr[left]
        right_s = arr[right] * arr[right]
        if left_s > right_s:
            squares.append(left_s)
            left += 1
        else:
            squares.append(right_s)
            right -= 1

    squares.reverse()
    return squares
