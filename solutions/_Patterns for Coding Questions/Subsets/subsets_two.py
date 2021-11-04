"""
Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:

    Input: [1,2,2]

    Output:
        [
        [2],
        [1],
        [1,2,2],
        [2,2],
        [1,2],
        []
        ]
https://leetcode.com/problems/subsets-ii/
"""
# https://leetcode.com/problems/permutations/discuss/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partioning
# also available here: https://github.com/paulonteri/patterns-for-coding-questions/blob/master/Subsets/subsets_with_duplicates.py
from typing import List


"""
- Sort all numbers of the given set. This will ensure that all duplicate numbers are next to each other.
- When we process a duplicate ( instead of adding the current number (which is a duplicate) to all the existing subsets,
		 only add it to the subsets which were created in the previous step.
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]):
        subsets = [[]]
        nums.sort()

        # used to mark the idx where the non duplicate subsets started being added
        last_num_added_start = 0
        for idx in range(len(nums)):
            subsets_length = len(subsets)

            # handle duplicates
            if idx > 0 and nums[idx] == nums[idx-1]:
                for index in range(last_num_added_start, subsets_length):
                    new_list = list(subsets[index])
                    new_list.append(nums[idx])
                    subsets.append(new_list)

            # non-duplicates
            else:
                for index in range(subsets_length):
                    new_list = list(subsets[index])
                    new_list.append(nums[idx])
                    subsets.append(new_list)

            last_num_added_start = subsets_length

        return subsets


class Solution00:
    def subsetsWithDup(self, nums: List[int]):
        nums.sort()
        res = [[]]

        last_added_count = 0
        for i, num in enumerate(nums):

            # # duplicates edge case
            # only add the duplicate to the subsets added previously in i-1
            if i > 0 and nums[i] == nums[i-1]:
                for idx in range(len(res)-last_added_count, len(res)):
                    res.append(res[idx] + [num])

            # # non-duplicates
            else:
                # is equal to the number of subsets to be added
                last_added_count = len(res)
                for idx in range(len(res)):
                    res.append(res[idx] + [num])

        return res
