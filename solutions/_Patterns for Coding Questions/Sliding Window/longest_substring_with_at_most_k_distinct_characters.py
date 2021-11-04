""" 
340. Longest Substring with At Most K Distinct Characters:

Given a string s and an integer k, 
return the length of the longest substring of s that contains at most k distinct characters.

Example 1:
    Input: s = "eceba", k = 2
    Output: 3
    Explanation: The substring is "ece" with length 3.
Example 2:
    Input: s = "aa", k = 1
    Output: 2
    Explanation: The substring is "aa" with length 2.

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
"""


import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int):
        if len(s) <= 0 or k == 0:
            return 0
        store = collections.defaultdict(int)

        idx = 0
        while idx < len(s) and len(store) < k:
            store[s[idx]] += 1
            idx += 1
        longest = idx

        left = 0
        for right in range(idx, len(s)):
            store[s[right]] += 1

            while len(store) > k:
                store[s[left]] -= 1
                if store[s[left]] == 0:
                    store.pop(s[left])
                left += 1

            longest = max(longest, (right-left)+1)

        return longest
