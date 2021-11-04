"""
Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:
    Input
        ["NumArray", "sumRange", "sumRange", "sumRange"]
        [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    Output
        [null, 1, -1, -3]
    Explanation
        NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
        numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
        numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
        numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

https://leetcode.com/problems/range-sum-query-immutable
"""


class NumArray:
    """ 
    Pre-compute the cumulative sums to give O(1) lookup
    """

    def __init__(self, nums):
        self.cumulative_sums = [0]*len(nums)

        running_sum = 0
        for idx, num in enumerate(nums):
            running_sum += num
            self.cumulative_sums[idx] = running_sum

    def sumRange(self, left: int, right: int):
        left_val = 0
        if left > 0:
            left_val = self.cumulative_sums[left-1]
        return self.cumulative_sums[right] - left_val


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
