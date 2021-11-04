""" 
Russian Doll Envelopes:

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
One envelope can fit into another if and only if both the width 
    and height of one envelope are greater than the other envelope's width and height.
Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
Note: You cannot rotate an envelope.

 

Example 1:
    Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
    Output: 3
    Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:
    Input: envelopes = [[1,1],[1,1],[1,1]]
    Output: 1

https://leetcode.com/problems/russian-doll-envelopes/
Based on: Longest Increasing Subsequence https://leetcode.com/problems/longest-increasing-subsequence
"""


class SolutionSLOW:  # time limit exceeded
    def maxEnvelopes(self, envelopes):
        items = list({tuple(item) for item in envelopes})
        items.sort(key=lambda x: x[0]+x[1])
        return self.longest_increasing_subsequence(items)

    def longest_increasing_subsequence(self, envelopes):
        dp = [1]*len(envelopes)

        for idx in reversed(range(len(dp))):
            largest = 0

            for i in range(idx+1, len(dp)):
                curr = envelopes[idx]
                nxt = envelopes[i]

                if curr[0] < nxt[0] and curr[1] < nxt[1]:
                    largest = max(dp[i], largest)

            dp[idx] = 1 + largest

        return max(dp)


""" 
"""


class Solution:
    def maxEnvelopes(self, arr):
        arr.sort(key=lambda x: (x[0], -x[1]))

        # extract the second dimension and run the LIS
        # already sorted by width
        return self.length_of_longest_increasing_subsequence([i[1] for i in arr])

    def length_of_longest_increasing_subsequence(self, nums):
        dp = [0] * len(nums)

        for right in range(len(nums)):
            largest_prev_subs = 0

            for left in range(right):
                if nums[right] > nums[left]:
                    #
                    largest_prev_subs = max(dp[left],  largest_prev_subs)

            dp[right] = largest_prev_subs + 1

        return max(dp)
