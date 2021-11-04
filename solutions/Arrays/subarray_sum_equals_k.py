"""
Subarray Sum Equals K

Given an array of integers and an integer k,
you need to find the total number of continuous subarrays whose sum equals to k.
Example 1:
    Input: nums = [1,1,1], k = 2
    Output: 2
Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2

https://leetcode.com/problems/subarray-sum-equals-k/
"""


from collections import defaultdict
from typing import List


"""

The idea behind the approach below is as follows: If the cumulative sum(represented by sum[i] for sum up to i^th index) up to two indices is the same,
 the sum of the elements lying in between those indices is zero.
Extending the same thought further, 
 if the cumulative sum up to two indices, say i and j is at a difference of k 
    i.e. if sum[i] - sum[j] = k, 
    the sum of elements lying between indices i and j is k.

If you were at a current sum, 
and you have seen (sum - k) before, it mean that,
we've seen an array of size k: - the distance between those two points is of size k
"""


# O(n) time | O(n) space | n = len(array)
class Solution:
    # check if a total sum in the past plus the current will be equal to k
    # if a (the current sum - a previous sum = k),
    # then elements in the array between must add up to k
    def subarraySum(self, nums: List[int], k: int):
        res = 0

        prev_sums = defaultdict(int)
        # the store has to have 0 to deal with the case where k is in the list
        prev_sums[0] = 1
        curr_sum = 0
        # if (the current sum - a sum in the past = k),
        # then the subarray in between them adds up to k
        for num in nums:

            curr_sum += num
            needed_diff = curr_sum - k

            # check for the needed_diff
            if needed_diff in prev_sums:
                # we add the number of possible times we can get that needed_diff
                res += prev_sums[needed_diff]

             # add the current sum to the store
            prev_sums[curr_sum] += 1

        return res


"""

# only works for arrays with positive integers
class Solution0:
    def subarraySum(self, nums: List[int], k: int):
        res = 0
        total = nums[0]

        start = end = 0
        while start < len(nums):
            if total == k:
                res += 1

            # # edge cases
            # when we cannot increase end or start
            if end == len(nums)-1 or start == len(nums)-1:
                total -= nums[start]
                start += 1
                continue

            if total <= k:
                end += 1
                total += nums[end]
            else:
                total -= nums[start]
                start += 1

        return res

"""
