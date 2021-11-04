""" 
Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
    Input: s = "12"
    Output: 2
    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:
    Input: s = "226"
    Output: 3
    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:
    Input: s = "0"
    Output: 0
    Explanation: There is no character that is mapped to a number starting with 0.
        The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
        Hence, there are no valid ways to decode this since all digits need to be mapped.
Example 4:
    Input: s = "06"
    Output: 0
    Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:
    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).

https://leetcode.com/problems/decode-ways
"""


""" 
https://www.notion.so/paulonteri/Recursion-DP-Backtracking-525dddcdd0874ed98372518724fc8753#fb64620280c74255982bb1d93455881b
"""


class Solution:
    def numDecodings(self, s: str):
        return self.helper(s, 0, [None]*len(s))

    def helper(self, s, idx, cache):
        if idx == len(s):
            return 1
        if cache[idx] is not None:
            return cache[idx]

        ways = 0

        if s[idx] != "0":
            # length one
            ways += self.helper(s, idx+1, cache)

            # length two
            if idx < len(s)-1:
                num = int(s[idx:idx+2])

                if num >= 1 and num <= 26:
                    ways += self.helper(s, idx+2, cache)

        cache[idx] = ways
        return cache[idx]


""" 
Bottom up DP
"""


class SolutionBU:
    def numDecodings(self, s: str):
        """ 
        What if s was of length 1? 2? 3? 4? ... n?
        """
        if not s or s[0] == "0":
            return 0

        # # create array to store the subproblem results ---------------------------------
        dp = [0]*len(s)
        dp[0] = 1
        # index 1: should handle 10, 11, 33, 30
        if len(s) >= 2:
            # Check if successful single digit decode is possible.
            if s[1] != '0':
                dp[1] = 1
            # Check if successful two digit decode is possible.
            two_digit = int(s[:2])
            if two_digit >= 10 and two_digit <= 26:
                dp[1] += 1

        # # fill in subproblem results ----------------------------------------------------------
        for i in range(2, len(dp)):
            # Check if successful single digit decode is possible.
            if s[i] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i-1: i+1])
            if two_digit >= 10 and two_digit <= 26:
                # result: dp[i] = dp[i - 1] + dp[i - 2]
                dp[i] += dp[i - 2]

        return dp[-1]


class SolutionBU2:
    def numDecodings(self, s: str):
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


""" 
Iterative, Constant Space
"""


class SolutionITER:
    def numDecodings(self, s: str):
        if s[0] == "0":
            return 0

        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back
