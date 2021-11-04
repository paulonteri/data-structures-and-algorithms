"""
Find the Missing Number:

We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:
    Input: [4, 0, 3, 1]
    Output: 2
Example 2:
    Input: [8, 3, 5, 2, 4, 6, 0, 1]
    Output: 7

"""


""" 
Since the input array contains unique numbers from the range 0 to ‘n’, 
    we can use a similar strategy as discussed in Cyclic Sort to place the numbers on their correct index.
Once we have every number in its correct place, 
    we can iterate the array to find the index which does not have the correct number, and that index will be our missing number.
"""


def find_missing_number(nums):
    idx = 0
    while idx < len(nums):
        num_in_range = nums[idx] >= 0 and nums[idx] < len(nums)
        if num_in_range and nums[idx] != idx:
            # nums[num-1], nums[idx] = nums[idx], nums[num-1]
            nums[nums[idx]], nums[idx] = nums[idx], nums[nums[idx]]
            continue
        idx += 1

    for idx in range(len(nums)):
        if nums[idx] != idx:
            return idx

    return -1
