"""
Three Sum. (3Sum):
Triplet Sum to Zero:

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

The solution set must not contain duplicate triplets.

Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
Example 2:

    Input: nums = []
    Output: []
Example 3:

    Input: nums = [0]
    Output: []

https://leetcode.com/problems/3sum/
https://www.educative.io/courses/grokking-the-coding-interview/gxk639mrr5r#try-it-yourself
https://github.com/paulonteri/leetcode/blob/master/Arrays/three_sum.py
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]):

        nums.sort()  # will make spotting of duplicates easy

        triplets = []
        length = len(nums)

        for i in range(length-2):  # ignore last two

            # check if element is a duplicate. the first cannot be a duplicate
            if i > 0 and nums[i] == nums[i-1]:
                # skip handling an element if it's similar to the one before it
                # because it is sorted, we effectively skip duplicates
                continue

            # TWO SUM for a sorted array
            # 1. find elements that will add up to 0
            # 2. check inner elements
            left = i + 1
            right = length - 1
            while left < right:

                # will be used to check if the sum is equal to 0
                total = nums[i] + nums[left] + nums[right]

                # if total is less than 0 we try to increase it's value
                if total < 0:
                    left += 1  # moving left to a larger value

                # if total is more than 0 we try to decrease it's value
                elif total > 0:
                    right -= 1  # moving right to a smaller value

                # 1. add list of elements to triplets
                # 2. check inner elements
                else:
                    # add elements to triplets
                    triplets.append([nums[i], nums[left], nums[right]])

                    # check inner elements
                    # 1. skip similar elements
                    # 2. move to inner elements

                    # skip:
                    # no need to continue with an element with the same value as l/r
                    # Skip all similar to the current left and right so that,
                    # when we are moving to the next element, we dont move to an element with the same value
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    # move to inner elements
                    left += 1
                    right -= 1

        return triplets


# O(n^2) time | O(n) space - where n is the length of the input array
def threeNumberSum(array, targetSum):
    triplets = []
    # help prevent duplicates and the result in triplets [] will be sorted
    array.sort()
    length = len(array)

    for idx, num in enumerate(array):

        # two sum
        left = idx + 1
        right = length - 1
        while left < right and right < length:
            total = num + array[left] + array[right]

            if total == targetSum:
                triplets.append([num, array[left], array[right]])
                right -= 1
                left += 1
            elif total > targetSum:
                right -= 1
            else:
                left += 1
    return triplets


"""
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = []
    Output: []

Example 3:
    Input: nums = [0]
    Output: []


Sorting the array will take O(N * logN)O(N∗logN). The searchPair/twoSum() function will take O(N)O(N). 
As we are calling searchPair() for every number in the input array, this means that overall searchTriplets() will take O(N * logN + N^2),
which is asymptotically equivalent to O(N^2)
"""
threeNumberSum([1, 2, 3, 4], 6)


class Solution00:
    def twoSum(self, nums, target, start_idx):
        res = []
        store = {}

        idx = start_idx
        while idx < len(nums):
            num = nums[idx]
            needed_num = target - num

            if needed_num in store:
                res.append([num, needed_num])
                store[num] = idx
                idx += 1

                # we skip these numbers as we have already recorded that they add up to the target (via res)
                #  we do not do this earlier in order to handle cases like;
                #   target=0, nums=[0,0], start_idx=0. The res should be [[0,0]]
                while idx < len(nums) and nums[idx] == num:
                    idx += 1

            else:
                store[num] = idx
                idx += 1

        return res

    def threeSum(self, nums: List[int]):
        nums.sort()
        res = []

        for idx in range(len(nums)-2):
            num = nums[idx]

            if idx > 0 and num == nums[idx-1]:
                continue

            for two_numbers in self.twoSum(nums, 0 - num, idx+1):
                res.append(two_numbers+[num])

        return res


class Solution01:
    def twoSum(self, nums, target, start_idx):
        res = []
        left, right = start_idx, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1

                # we skip these numbers as we have already recorded that they add up to the target (via res)
                #  we do not do this earlier in order to handle cases like;
                #   target=0, nums=[0,0], start_idx=0. The res should be [[0,0]]
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

        return res

    def threeSum(self, nums: List[int]):
        nums.sort()
        res = []

        for idx in range(len(nums)-2):
            num = nums[idx]

            if idx > 0 and num == nums[idx-1]:
                continue

            for two_numbers in self.twoSum(nums, 0 - num, idx+1):
                res.append(two_numbers+[num])

        return res
