"""
Reverse Integer:

Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x):
        res = 0

        num = abs(x)
        while num > 0:
            last_digit = num % 10  # get last digit
            res = (10 * res) + last_digit

            num //= 10  # remove last digit

        # confirm 32-bit signed integer
        if res < -2**31 or res > 2**31-1:
            return 0

        #
        if x < 0:
            return -res
        return res


class SolutionB:
    def reverse(self, x: int):

        # check if negative
        negative = False
        if x < 0:
            negative = True

        num = list(str(x))
        rev_num = []

        # skip the minus sign(for negative values)
        length = len(num)
        maximum = length
        if negative:
            maximum = length - 1

        # reverse each character
        i = 0
        while i < maximum:
            rev_num.append(num.pop())
            i += 1

        # create new integer
        res = int("".join(rev_num))
        if negative:
            res = -res

        # confirm 32-bit signed integer
        if res < -2**31 or res > 2**31-1:
            return 0
        return res
