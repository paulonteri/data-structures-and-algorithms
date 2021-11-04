""" 
Find All Numbers Disappeared in an Array:

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]
Example 2:
    Input: nums = [1,1]
    Output: [2]

Constraints:
    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        result = []

        idx = 0
        while idx < len(nums):
            num = nums[idx]
            if num-1 != idx and nums[num-1] != num:
                nums[num-1], nums[idx] = nums[idx], nums[num-1]
                continue
            idx += 1

        for idx in range(len(nums)):
            if nums[idx]-1 != idx:
                result.append(idx+1)

        return result
