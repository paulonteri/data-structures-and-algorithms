""" 
Find First and Last Position of Element in Sorted Array/Search For Range:

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]
Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]


https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
https://www.algoexpert.io/questions/Search%20For%20Range
"""


""" 

- find the number using binary search
- find start of range using binary search
- find end of range using binary search

[0,1,2,3,4,5]
[5,7,7,8,8,10] 8


[0, 1, 2,   3,  4,  5   6,   7  8   9  10  11  12]
[0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73] 45

# find end
l, r  m
6, 12 9
10,12 11
10,10 10


"""

""" 
Simplest using pointers to remember last seen
"""


class Solution_P:
    def searchRange(self, nums, target):
        return [
            self.find_start(nums, target),
            self.find_end(nums, target)
        ]

    def find_start(self, nums, target):
        last_seen = -1

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # record that we have seen it &
                #  ignore everything to the right
                last_seen = mid
                right = mid - 1
        return last_seen

    def find_end(self, nums, target):
        last_seen = -1

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # record that we have seen it &
                #  ignore everything to the left
                last_seen = mid
                left = mid + 1
        return last_seen


""" 


"""


class Solution00:
    def searchRange(self, nums, target):

        # # find target
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break

        mid = (left+right)//2
        if mid < 0 or mid >= len(nums) or nums[mid] != target:
            return [-1, -1]

        # # find start of range
        start_left = 0
        start_right = mid
        while start_left < start_right:

            start_mid = (start_left+start_right)//2
            # ensure start_right's value always == target,
            #   when start_left == start_right, that will be the leftmost value with a value of target
            if nums[start_mid] == target:
                start_right = start_mid
            else:
                start_left = start_mid + 1

        # # find end of range
        end_left = mid
        end_right = len(nums)-1
        while end_left <= end_right:
            # print(end_left, end_right)
            end_mid = (end_right+end_left)//2
            # ensure end_left's value always == target,
            #   when end_right == end_left, that will be the rightmost value with a value of target
            if nums[end_mid] == target:
                end_left = end_mid + 1
            else:
                end_right = end_mid - 1

        # #
        return [start_left, end_right]


"""
improvement of above, same time complexity
"""


class Solution:
    def searchRange(self, nums, target):

        # # find start of range
        start_left = 0
        start_right = len(nums)-1
        while start_left < start_right:

            start_mid = (start_left+start_right)//2

            # 1. place start_right in the target subarray
            if nums[start_mid] > target:
                start_right = start_mid
                continue

            # 2. ensure start_right's value always == target,
            #       when start_left == start_right, that will be the leftmost value with a value of target
            if nums[start_mid] == target:
                start_right = start_mid
            else:
                start_left = start_mid + 1

        # # find end of range
        end_left = 0
        end_right = len(nums)-1
        while end_left <= end_right:
            end_mid = (end_right+end_left)//2

            # 1. place end_left in the target subarray
            if nums[end_mid] < target:
                end_left = end_mid + 1
                continue

            # 2. find the first value not equal to target on the end_left pointer
            #       then move the end_right - 1 coz end_left will be +1 position ahead of the last correct value
            if nums[end_mid] == target:
                end_left = end_mid + 1
            else:
                end_right = end_mid - 1

        if end_right < 0 or start_left >= len(nums) or nums[start_left] != target or nums[end_right] != target:
            return [-1, -1]

        # #
        return [start_left, end_right]
