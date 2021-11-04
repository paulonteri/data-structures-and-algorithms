""" 
Strobogrammatic Number

Given a string num which represents an integer, return true if num is a strobogrammatic number.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).


Example 1:
    Input: num = "69"
    Output: true
Example 2:
    Input: num = "88"
    Output: true
Example 3:
    Input: num = "962"
    Output: false
Example 4:
    Input: num = "1"
    Output: true

https://leetcode.com/problems/strobogrammatic-number
"""


class Solution:
    def isStrobogrammatic(self, num):
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        rotated = list(num)
        for idx, char in enumerate(rotated):
            if char not in rotated_digits:
                return False

            rotated[idx] = rotated_digits[char]

        rotated.reverse()
        return "".join(rotated) == num
