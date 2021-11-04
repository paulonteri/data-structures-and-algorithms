"""
First Unique Character in a String

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
You may assume the string contains only lowercase English letters.

https://www.algoexpert.io/questions/First%20Non-Repeating%20Character
"""


# O(1) Space | alphabet has 26 chars
# O(n) Time | n = len(string)
class Solution:
    def firstUniqChar(self, s: str):

        # store the unique chars and the no. of times they appear
        store = {}

        # record no. of times chars appear
        for char in s:

            if char in store:
                store[char] = store[char] + 1

            else:
                store[char] = 1

        # return earliest non-repeating character
        for i, char in enumerate(s):

            if store[char] == 1:  # means it only appeared once
                return i

        return -1
