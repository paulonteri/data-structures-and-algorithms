""" 
Next Permutation:

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, 
    it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]
Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]
Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]
Example 4:
    Input: nums = [1]
    Output: [1]


Needs many examples to understand
Drawing a chart of heaps and valleys can make it a bit easier to understand

[1,3,2] => [2,1,3]

[1,2,3,4] => [1,2,4,3]
[4,1,2,3] => [4,1,3,2]
[3,4,2,1] => [4,1,2,3] - swapped 3 & 4 then sorted the numbers to the right of 4
[2,3,4,1] => [2,4,1,3] - swapped 3 & 4 then sorted the numbers to the right of 4

[15,2,--4--,6,--5--,2] => [15,2,--5--,2,4,6] - swapped 4 & 5 then sorted the numbers to the right of 5

https://leetcode.com/problems/next-permutation/
https://www.notion.so/paulonteri/Math-Tricks-8c99fd21a1d343f7bee1eaf0467ea362#4bda6bec59634b1ebf5bc34fb2edc542

similar to https://leetcode.com/problems/maximum-swap
"""


class Solution:
    def nextPermutation(self, nums):
        """
        1. look for peak that has its larger & smaller number furthest to the right
            - Note: peak => num[right] > num[left]
            - find first smaller number (furthest to the right)
            - then find the number furthest to the right that is larger than it
            - swap the smaller and larger
        2. if no peak was found srt the whole array and return
        3. sort the array to the right of where the larger number was placed 

        """
        small_num_idx = None

        # find first smaller number (furthest to the right)
        i = len(nums)-1
        largest = nums[-1]
        while not small_num_idx and i >= 0:
            if nums[i] < largest:
                small_num_idx = i
            largest = max(largest, nums[i])
            i -= 1

        # array is sorted in descending order
        if small_num_idx is None:
            nums.sort()
            return

        # find number (furthest to the right) larger than small_num
        for idx in reversed(range(small_num_idx+1, len(nums))):
            if nums[idx] > nums[small_num_idx]:
                # swap larger and smaller number
                nums[small_num_idx], nums[idx] = nums[idx], nums[small_num_idx]
                # sort area after where the larger swapped number was placed
                self.sort(nums, small_num_idx+1)

                return

    def sort(self, nums, sort_start):
        # nums[sort_start:] = list(sorted(nums[sort_start:]))
        for idx in range(sort_start, len(nums)):
            smallest = idx
            for i in range(idx, len(nums)):
                if nums[i] < nums[smallest]:
                    smallest = i
            nums[smallest], nums[idx] = nums[idx], nums[smallest]
