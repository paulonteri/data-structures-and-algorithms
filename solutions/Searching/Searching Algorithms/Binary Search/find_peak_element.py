""" 
Find Peak Element

A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

https://leetcode.com/problems/find-peak-element/
"""


""" 
[1,2,3,1]   => 2
[1,2,3,4,5] => 4
[5,4,3,2,1] => 0

Binary search:
    - if the element at mid is in an increasing order:
        - if we move to the right, we might find a peak(decreases) or the array end 
            which are both valid answers
    - the opposite is also True
"""


class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2

            # ends (also is peak)
            if mid == 0:
                if nums[mid+1] < nums[mid]:
                    return mid
                left = mid + 1
            elif mid == len(nums)-1:
                if nums[mid-1] < nums[mid]:
                    return mid
                right = mid

            # is peak but not on ends
            elif nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid

            # is increasing
            elif nums[mid-1] < nums[mid]:
                left = mid + 1

            # is increasing
            else:
                right = mid
