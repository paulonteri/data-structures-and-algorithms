""" 
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or 
 no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4
Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

https://leetcode.com/problems/longest-increasing-subsequence/
"""

"""

[9] => 1

[8,9] => 2

[7,8,0,9] => 2

"""


class Solution:
    def lengthOfLIS(self, nums):
        result = 0

        cache = [None]*len(nums)
        # subsequence can start at any element
        for idx in range(len(nums)):
            result = max(self.helper(nums, idx, cache), result)

        return result

    def helper(self, nums, idx, cache):
        if cache[idx] is not None:
            return cache[idx]

        result = 1  # smallest subsequence for each number
        # next larger may be any larger element to the right
        for i in range(idx+1, len(nums)):
            if nums[i] > nums[idx]:
                result = max(1+self.helper(nums, i, cache), result)

        cache[idx] = result
        return cache[idx]

    # def lengthOfLIS(self, nums):
    #     cache = [None]*len(nums)
    #     for idx in range(len(nums)):
    #         self.helper(nums, idx, cache)
    #     return max(cache)


""" 
[10,9,2,5,3,7,101,18]

[ 2,2,4,3,3,2, 1, 1]
"""


class Solution_Tabulation_1:
    def lengthOfLIS(self, nums):
        dp = [1]*len(nums)

        for idx in reversed(range(len(dp))):
            largest = 0

            for i in range(idx+1, len(dp)):
                if nums[i] > nums[idx]:
                    largest = max(dp[i], largest)

            dp[idx] = 1 + largest

        return max(dp)


""" 
[10, 9, 2, 5, 3, 7, 101, 18]
[ 0, 1, 2, 3, 4, 5,   6,  7]

0
[ 1, 1, 1, 1, 1, 1,   1,  1]
1
[ 1, 1, 1, 1, 1, 1,   1,  1]
2
[ 1, 1, 1, 1, 1, 1,   1,  1]
3 values smaller than 5 => 2
[ 1, 1, 1, 2, 1, 1,   1,  1]
4 values smaller than 3 => 2
[ 1, 1, 1, 2, 2, 1,   1,  1]
5 values smaller than 7 => 2,5,3
[ 1, 1, 1, 2, 2, 3,   1,  1]
6 values smaller than 101 => 2,5,3,7
[ 1, 1, 1, 2, 2, 3,   4,  1]
7 values smaller than 18 => 2,5,3,7
[ 1, 1, 1, 2, 2, 3,   4,  4]


1. Initialize an array dp with length nums.length and all elements equal to 1. 
    dp[i] represents the length of the longest increasing subsequence that ends with the element at index i.

2. Iterate from i = 1 to i = nums.length - 1. 
    At each iteration, use a second for loop to iterate from j = 0 to j = i - 1 (all the elements before i). 
    For each element before i, check if that element is smaller than nums[i]. 
    If so, set dp[i] = max(dp[i], dp[j] + 1).

3. Return the max value from dp.

"""


class Solution_Tabulation_2:
    def lengthOfLIS(self, nums):
        dp = [0] * len(nums)

        for right in range(len(nums)):
            largest_prev_subs = 0

            for left in range(right):
                if nums[right] > nums[left]:
                    #
                    largest_prev_subs = max(
                        dp[left],  largest_prev_subs)

            dp[right] = largest_prev_subs + 1

        return max(dp)

    def lengthOfLIS_2(self, nums):
        dp = [1] * len(nums)

        for curr_idx in range(1, len(nums)):
            for prev_idx in range(curr_idx):

                if nums[curr_idx] > nums[prev_idx]:

                    dp[curr_idx] = max(
                        dp[curr_idx],
                        dp[prev_idx] + 1
                    )

        return max(dp)
