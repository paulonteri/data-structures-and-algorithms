"""
Find Minimum in Rotated Sorted Array:

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums, return the minimum element of this array.

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

After this: Search in Rotated Sorted Array https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


class Solution:
    # search for the beginning of the unsorted part
    def findMin(self, nums):
        if not nums:
            return None

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2

            # look for the beginning of the unsorted part
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # Binary Search
            if nums[mid] > nums[right]:  # check if right side is unsorted
                left = mid + 1
            else:
                right = mid - 1

        # return smallest number
        return nums[left]


"""
[3,4,5,1,2]
[4,5,6,7,0,1,2]
[11,13,15,17]
[11,13,15,17,10]
[1]
[3,1,2]
"""
