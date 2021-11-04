""" 
Missing Number:


Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Example 4:
    Input: nums = [0]
    Output: 1
    Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.


https://leetcode.com/problems/missing-number/
"""

""" 
Sum formulae:

(sum of all possible numbers) - (sum of given number) = missing_number
"""


class Solution0:
    def missingNumber(self, nums):

        possible = sum(range(len(nums)+1))
        given = sum(nums)

        return possible - given


""" 
Bitwise XOR 
4^4=0          -> cancel out each other
4^0=4
4^7^6^6^4^7=0  -> contains all the pairs
4^7^6^4^7=6    -> missing pair of 6


- XOR all the possible numbers with the given numbers, 
    the result will be the missing as it won't have a partner to cancel it out

example: [3,0,1]
- > all possible: 0^1^2^3
- > given: 3^0^1
- > 0^1^2^3 ^ 3^0^1 = 2 (it won't be canceled out)
"""


class Solution:
    def missingNumber(self, nums):

        res = 0
        for i in range(1, len(nums)+1):
            res ^= i

        for num in nums:
            res ^= num

        return res
