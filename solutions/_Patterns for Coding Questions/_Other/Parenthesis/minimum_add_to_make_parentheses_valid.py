""" 
921. Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:
    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
You are given a parentheses string s. 
In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
Example 3:

Input: s = "()"
Output: 0
Example 4:

Input: s = "()))(("
Output: 4

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid
"""


class Solution:
    def minAddToMakeValid(self, s: str):
        invalid_closing = 0
        invalid_opening = 0

        # invalid closing
        opening_remaining = 0
        for char in s:
            if char == "(":
                opening_remaining += 1
            else:
                if opening_remaining > 0:
                    opening_remaining -= 1
                else:
                    invalid_closing += 1

        # invalid closing
        closing_remaining = 0
        for idx in reversed(range(len(s))):
            if s[idx] == ")":
                closing_remaining += 1
            else:
                if closing_remaining > 0:
                    closing_remaining -= 1
                else:
                    invalid_opening += 1

        return invalid_opening + invalid_closing
