""" 
Permutations II

Given a collection of numbers, nums, that might contain duplicates,
 return all possible unique permutations in any order.

Example 1:
    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
    [1,2,1],
    [2,1,1]]
Example 2:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

https://leetcode.com/problems/permutations-ii
"""

import collections


class Solution:
    def permuteUnique(self, nums):
        result = []
        self.dfs(collections.Counter(nums), len(nums), [], result)
        return result

    def dfs(self, numbers, length, curr, result):
        if len(curr) == length:
            result.append(curr)

        for num in numbers:
            if numbers[num] == 0:
                continue

            numbers[num] -= 1
            self.dfs(numbers, length, curr+[num], result)

            # backtrack
            numbers[num] += 1
