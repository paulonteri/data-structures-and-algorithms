"""
Shortest Unsorted Continuous Subarray:

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order,
 then the whole array will be sorted in ascending order.
Return the shortest such subarray and output its length.

Example 1:
    Input: nums = [2,6,4,8,10,9,15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:
    Input: nums = [1,2,3,4]
    Output: 0
Example 3:
    Input: nums = [1]
    Output: 0

https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
https://www.algoexpert.io/questions/Subarray%20Sort
"""


"""
[2,6,4,8,10,9,15]
- iterate through the array starting from the left:
    - each value should be larger or equal to all on the left
    - keep track of the largest values you see
    - if you find any value smaller that that move the right pointer there (9)
- iterate through the array starting from the right:
    - keep track of the smallest values you see
    - if you find any value larger that that move the left pointer there (6)
    
return (right - left) + 1
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        left = 0
        right = 0

        minimum = nums[0]
        for idx in range(len(nums)):
            if nums[idx] < minimum:
                right = idx
            minimum = max(nums[idx], minimum)

        maximum = nums[-1]
        for idx in reversed(range(len(nums))):
            if nums[idx] > maximum:
                left = idx
            maximum = min(nums[idx], maximum)

        if right == 0 and left == 0:
            return 0
        return right - left + 1
