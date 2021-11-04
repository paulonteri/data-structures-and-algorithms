""" 
Cyclic Sort:

We are given an array containing ‘n’ objects. 
Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space. 
For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

There are no duplicates

Example 1:
    Input: [3, 1, 5, 4, 2]
    Output: [1, 2, 3, 4, 5]
Example 2:
    Input: [2, 6, 4, 3, 1, 5]
    Output: [1, 2, 3, 4, 5, 6]
Example 3:
    Input: [1, 5, 6, 4, 3, 2]
    Output: [1, 2, 3, 4, 5, 6]
"""


"""
As we know, the input array contains numbers in the range of 1 to ‘n’. We can use this fact to devise an efficient way to sort the numbers. 
Since all numbers are unique, we can try placing each number at its correct place, i.e., placing ‘1’ at index ‘0’, placing ‘2’ at index ‘1’, and so on.
"""


def cyclic_sort(nums):

    idx = 0
    while idx < len(nums):
        if nums[idx] != idx+1:
            # nums[num-1], nums[idx] = nums[idx], nums[num-1]
            nums[nums[idx]-1], nums[idx] = nums[idx], nums[nums[idx]-1]
            continue

        idx += 1

    return nums
