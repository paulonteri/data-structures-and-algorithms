"""
Binary Search:

Write a function that takes in a sorted array of integers as well as a target integer. 
The function should use the Binary Search algorithm to determine if the target integer is contained in the array and
 should return its index if it is, otherwise -1.

https://leetcode.com/explore/learn/card/binary-search/
"""


# O(log(n)) time | O(1) space
def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:  # found num
            return mid

        elif target > array[mid]:  # num is to the right of mid
            left = mid + 1
        else:  # num is to the left of mid
            right = mid - 1

    return -1


"""
The Binary Search algorithm works by finding the number in the middle of the input array and comparing it to the target number.
Given that the array is sorted, if this middle number is smaller than the target number,
then the entire left part of the array is no longer worth exploring since the target number can no longer be in it;
similarly, if the middle number is greater than the target number, then the entire right part of the array is no longer worth exploring.
Applying this logic recursively eliminates half of the array until the number is found or until the array runs out of numbers.
"""


class Solution:
    def search(self, nums, target):

        if not nums:
            return

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            return left
        return -1


def binarySearch2(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1
