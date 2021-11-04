"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

https://leetcode.com/problems/valid-anagram/
"""


# 0(n) time | O(1) space
class Solution:
    def isAnagram(self, s: str, t: str):

        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        # chars from s will be added as +1
        # chars from t will be added as -1
        # then we check if each char will have a total of 0
        store = {}

        # add chars to store
        for i in range(len_s):

            # s
            if s[i] not in store:
                store[s[i]] = 1
            else:
                store[s[i]] = store[s[i]] + 1

            # t
            if t[i] not in store:
                store[t[i]] = -1
            else:
                store[t[i]] = store[t[i]] - 1

        # check if each character in the store has a value of 0
        for char in s:
            if store[char] != 0:
                return False

        return True


"""
Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false
"""
