""" 
Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

https://leetcode.com/problems/jump-game
"""

""" 
Top down:
try every single jump pattern that takes us from the first position to the last. 
We start from the first position and jump to every index that is reachable. 
We repeat the process until last index is reached. When stuck, backtrack.

One quick optimization we can do for the code above is to check the nextPosition from right to left. (jump furthest)
The theoretical worst case performance is the same, but in practice, for silly examples, the code might run faster. 
Intuitively, this means we always try to make the biggest jump such that we reach the end as soon as possible

Top-down Dynamic Programming can be thought of as optimized backtracking. 
It relies on the observation that once we determine that a certain index is good / bad, this result will never change. 
This means that we can store the result and not need to recompute it every time.
Therefore, for each position in the array, we remember whether the index is good or bad. 

O(n^2) time | O(2n) == O(n) space
"""


class SolutionMEMO:  # TLE
    def canJump(self, nums):

        return self.jump_helper(nums, [None]*len(nums), 0)

    def jump_helper(self, nums, cache, idx):
        if idx >= len(nums)-1:
            return True
        if cache[idx] is not None:
            return cache[idx]

        for i in reversed(range(idx+1, idx+nums[idx]+1)):
            if self.jump_helper(nums, cache, i):
                cache[idx] = True
                return cache[idx]

        cache[idx] = False
        return cache[idx]


""" 
Bottom up:
Top-down to bottom-up conversion is done by eliminating recursion. 
In practice, this achieves better performance as we no longer have the method stack overhead and might even benefit from some caching. 
More importantly, this step opens up possibilities for future optimization. 
The recursion is usually eliminated by trying to reverse the order of the steps from the top-down approach.

The observation to make here is that we only ever jump to the right. 
This means that if we start from the right of the array, every time we will query a position to our right, that position has already be determined as being GOOD or BAD. 
This means we don't need to recurse anymore, as we will always hit the memo/cache table.

O(n^2) time | O(n) space


-------------------------------------------------------------------------------------------------------------------------

Greedy

Once we have our code in the bottom-up state, we can make one final, important observation. 
From a given position, when we try to see if we can jump to a GOOD position, we only ever use one - the first one. 
    In other words, the left-most one. 
If we keep track of this left-most GOOD position as a separate variable, we can avoid searching for it in the array. 
    Not only that, but we can stop using the array altogether.

https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/506853/Java-A-general-greedy-solution-to-process-similar-problems

O(n) time | O(1) space
"""


class SolutionBU:
    def canJump(self, nums):
        dp = [None]*len(nums)
        dp[-1] = True

        for idx in reversed(range(len(nums)-1)):

            for idx_2 in range(idx+1, idx+nums[idx]+1):
                if dp[idx_2] == True:
                    dp[idx] = True
                    break

        return dp[0]


class Solution:
    def canJump(self, nums):

        last_valid = len(nums)-1
        for idx in reversed(range(len(nums)-1)):

            if idx+nums[idx] >= last_valid:
                last_valid = idx

        return last_valid == 0
