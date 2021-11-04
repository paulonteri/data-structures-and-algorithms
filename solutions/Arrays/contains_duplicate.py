""" 
Contains Duplicate

Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    def containsDuplicate(self, nums):

        store = set()

        for num in nums:
            # we have seen num before
            if num in store:
                return True
            # record that we have just seen num
            store.add(num)

        return False


class Solution_:
    def containsDuplicate(self, nums):
        nums.sort()

        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx-1]:
                return True

        return False
