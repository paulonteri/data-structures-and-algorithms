"""
Longest Substring Without Repeating Characters: Leetcode 3

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution(object):
    # O(n) time | O(n) space | n=len(s)
    def lengthOfLongestSubstring(self, s):

        # we will use a 'sliding window' algorithm
        # window pointers
        start = 0
        end = 0

        # store values for the current 'window'
        store = {}

        longest = 0

        while end < len(s) and start <= end:

            # seen value before (in current substring)
            # shorten/narrow down substring by moving the front pointer forward & removing it from the store,
            # this is done till we have no more repeating characters
            if s[end] in store:
                store.pop(s[start])
                start += 1

            # not seen value before (in current substring)
            # increase the size of the sliding window
            # add value to store & increase longest's value
            else:
                store[s[end]] = True  # add to store
                end += 1  # move on to next

                # ensure the longest's value sticks to the highest we will ever find
                # keep track of the longest string
                # will remain at the highest value we ever found
                # note that the number of items in the store usually decreases
                longest = max(longest, len(store))

        return longest


"""
Example Testcases:

Example 1:
    Input: s = "abcabcbb"
    Output: 3

Example 2:
    Input: s = "bbbbb"
    Output: 1
"""
