""" 
1328. Break a Palindrome

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.
Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.
A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. 
For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

Example 1:
    Input: palindrome = "abccba"
    Output: "aaccba"
    Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
    Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:
    Input: palindrome = "a"
    Output: ""
    Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
Example 3:
    Input: palindrome = "aa"
    Output: "ab"
Example 4:
    Input: palindrome = "aba"
    Output: "abb"

https://leetcode.com/problems/break-a-palindrome
https://youtu.be/MWHz4yjOSKM
"""


class Solution:
    def breakPalindrome(self, palindrome: str):
        if len(palindrome) <= 1:
            return ""

        # replace first non-a
        is_odd = len(palindrome) % 2 != 0
        for idx, char in enumerate(palindrome):
            if is_odd and idx == len(palindrome) // 2:
                continue

            if char != "a":
                return palindrome[:idx] + "a" + palindrome[idx+1:]

        # no valid non-a was found so replace the last character
        # eg: aaa->aab, aaaa->aaab, aba->abb
        return palindrome[:-1] + "b"
