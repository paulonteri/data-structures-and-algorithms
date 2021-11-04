""" 
Single Number:

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

https://leetcode.com/problems/single-number/
"""


""" 
4^4=0          -> cancel out each other
4^0=4
4^7^6^6^4^7=0  -> contains all the pairs
4^7^6^4^7=6    -> missing pair of 6

"""


class Solution:
    def singleNumber(self, nums):

        res = 0
        for num in nums:
            res ^= num
        return res
