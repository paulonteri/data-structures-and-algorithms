""" 
Search in Rotated Sorted Array:

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
Example 3:
    Input: nums = [1], target = 0
    Output: -1

https://leetcode.com/problems/search-in-rotated-sorted-array/
https://www.algoexpert.io/questions/Shifted%20Binary%20Search

Prerequisite: Find Minimum in Rotated Sorted Array https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


class Solution_:
    def search(self, nums, target):

        start_idx = self.get_smallest_num_idx(nums)

        if target >= nums[start_idx] and target <= nums[-1]:
            return self.binary_search(nums, target, start_idx, len(nums)-1)
        return self.binary_search(nums, target, 0, start_idx)

    def get_smallest_num_idx(self, nums):

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2

            if mid > 0 and nums[mid-1] > nums[mid]:
                return mid
            if mid < len(nums)-1 and nums[mid+1] < nums[mid]:
                return mid+1

            # if right is unsorted
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


""" 
- we know that:
    - If a section (left-mid or mid-right) is unsorted then the other must be sorted

"""


class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # left is sorted
                if target >= nums[left] and target <= nums[mid]:  # in left
                    right = mid
                else:
                    left = mid + 1

            else:  # right is sorted
                if target >= nums[mid] and target <= nums[right]:  # in right
                    left = mid
                else:
                    right = mid - 1

        return -1
