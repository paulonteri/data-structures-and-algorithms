"""
Move Zeroes:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

https://leetcode.com/problems/move-zeroes/
"""


# 0(n) time | 0(1) space
class Solution:
    def moveZeroes(self, nums):

        # # reorder list skipping all zeros (The first one might be replaced by itself if it's not 0)
        next_none_zero = 0  # will mark the next char to be replaced
        for i in range(len(nums)):

            # replace --> if the current char is 0 it will not replace the prev
            if nums[i] != 0:
                nums[next_none_zero] = nums[i]
                next_none_zero += 1

        # from where the next_none_zero last stuck,
        # replace all the nums from the next_none_zero to the end with 0
        while next_none_zero < len(nums):
            nums[next_none_zero] = 0
            next_none_zero += 1
