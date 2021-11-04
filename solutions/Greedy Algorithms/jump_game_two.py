""" 
45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: 2
    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
    Input: nums = [2,3,0,1,4]
    Output: 2

https://leetcode.com/problems/jump-game-ii

Prerequisites:
- https://leetcode.com/problems/jump-game
"""

""" 
DP Memoization
"""


class SolutionMEMO:
    def jump(self, nums):
        cache = [None]*len(nums)
        cache[-1] = 0

        self.jump_helper(nums, 0, cache)

        return cache[0]

    def jump_helper(self, nums, idx, cache):
        if idx >= len(nums):
            return 0
        if cache[idx] is not None:
            return cache[idx]

        result = float('inf')
        for i in range(idx+1, idx+nums[idx]+1):
            result = min(result, self.jump_helper(nums, i, cache))

        result += 1  # add current jump

        cache[idx] = result
        return cache[idx]


""" 
DP Bottom up
"""


class Solution:
    def jump(self, nums):
        cache = [None]*len(nums)
        cache[-1] = 0

        for idx in reversed(range(len(nums)-1)):
            if nums[idx] != 0:
                cache[idx] = min(cache[idx+1:idx+nums[idx]+1]) + 1
            else:
                cache[idx] = float('inf')

        return cache[0]


""" 
Greedy
https://www.notion.so/paulonteri/Greedy-Algorithms-b9b0a6dd66c94e7db2cbbd9f2d6b50af#255fab0c8c0242df8f7e53d9ec2a83b8
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/506853/Java-A-general-greedy-solution-to-process-similar-problems
"""


class Solution_:
    def jump(self, nums):
        result = 0

        current_jump_end = 0
        farthest_possible = 0  # furthest jump we made/could have made
        for i in range(len(nums) - 1):

            # we continuously find the how far we can reach in the current jump
            # record the futhest point accessible in our current jump
            farthest_possible = max(farthest_possible, i + nums[i])

            # if we have come to the end of the current jump, we need to make another jump
            if i == current_jump_end:
                result += 1
                # move to the furthest possible point
                current_jump_end = farthest_possible

        return result


class Solution:
    def jump(self, nums):
        result = 0

        i = 0
        farthest_possible = 0  # furthest jump we made/could have made
        while i < len(nums) - 1:
            # # create new jump & move to the furthest possible point
            farthest_possible = max(farthest_possible, i + nums[i])
            # new jump - jump furthest
            result += 1
            current_jump_end = farthest_possible
            # next
            i += 1

            # # move to end of current jump
            while i < len(nums) - 1 and i < current_jump_end:
                # we continuously find the how far we can reach in the current jump
                # record the futhest point accessible in our current jump
                farthest_possible = max(farthest_possible, i + nums[i])
                i += 1

        return result
