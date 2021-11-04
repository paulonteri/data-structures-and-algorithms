""" 
Valid Palindrome II:

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
    Input: s = "aba"
    Output: true
Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.
Example 3:
    Input: s = "abc"
    Output: false

https://leetcode.com/problems/valid-palindrome-ii
"""


class Solution:
    def validPalindrome(self, s: str):

        left = 0
        right = len(s)-1
        while left < right:
            # left and right are same
            if s[left] == s[right]:
                left += 1
                right -= 1

            # left and right not same
            else:
                return self.isPalindrome(s, left) or self.isPalindrome(s, right)

        return True

    def isPalindrome(self, s, skip):
        # we will start be comparing the left most char & the right most char
        a_pointer = 0
        b_pointer = len(s) - 1

        while a_pointer < b_pointer:
            # skip
            if a_pointer == skip:
                a_pointer += 1
            if b_pointer == skip:
                b_pointer -= 1

            # check if not the same
            if s[a_pointer] != s[b_pointer]:
                return False

            # move on to the next set of chars
            a_pointer += 1
            b_pointer -= 1
        return True
