""" 
Longest Consecutive Sequence:

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109

https://www.algoexpert.io/questions/Largest%20Range
https://leetcode.com/problems/longest-consecutive-sequence/
"""
""" 
Largest Range:

Write a function that takes in an array of integers and 
    returns an array of length 2 representing the largest range of integers contained in that array.
The first number in the output array should be the first number in the range, 
    while the second number should be the last number in the range.
A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. 
For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. 
Note that numbers don't need to be sorted or adjacent in the input array in order to form a range.
You can assume that there will only be one largest range.
Sample Input
    array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Sample Output
    [0, 7]
"""


# O(nlog(n)) time
def largestRange(nums):
    if len(nums) < 1:
        return []

    nums.sort()
    res = [0, 0]

    idx = 0
    while idx < len(nums) - 1:
        # check if start of consecutive nums
        if not (nums[idx]+1 == nums[idx+1] or nums[idx] == nums[idx+1]):
            idx += 1
            continue

        # find the numbers
        end = idx+1
        while end < len(nums)-1 and (nums[end]+1 == nums[end+1] or nums[end] == nums[end+1]):
            end += 1

        # record
        res = max(res, [idx, end], key=lambda x: nums[x[1]] - nums[x[0]])

        # move pointer
        idx = end

    return [nums[res[0]], nums[res[1]]]


""" 
------------------------------------------------------------------------------------------------------------------------------------------------

- for each number try to build the largest number range from the input array
- the numbers can be stored in a set to improve lookup time

- for each num, if num-1 is in the set:
    - do not check the num because it will be in num-1's range

"""


# O(n) time
class Solution:
    def longestConsecutive(self, nums):
        longest = 0

        store = set(nums)

        for num in store:
            if num-1 in store:
                # do not check the num because it will be in num-1's range
                continue

            # try to build the largest consecutive sequence from the input array
            count = 1
            while num+1 in store:
                count += 1
                num += 1

            longest = max(count, longest)

        return longest
