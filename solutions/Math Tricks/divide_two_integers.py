""" 
Divide Two Integers:

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

 

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:
    Input: dividend = 0, divisor = 1
    Output: 0
Example 4:
    Input: dividend = 1, divisor = 1
    Output: 1

https://leetcode.com/problems/divide-two-integers
"""


class SolutionBF:
    def divide(self, dividend: int, divisor: int):
        is_neg = False
        if divisor < 0:
            divisor = abs(divisor)
            is_neg = not is_neg
        if dividend < 0:
            dividend = abs(dividend)
            is_neg = not is_neg

        count = 0
        while dividend >= divisor:
            dividend -= divisor
            count += 1

        if is_neg:
            return -count
        return count


""" 
dividend = 28, divisor = 3

Repeated Exponential Searches
- Keep on doubling divisor till it cannot be doubled more
3  =3       =3*2^0
6  =3*2     =3*2^1
12 =3*2*2   =3*2^2
24 =3*2*2*2 =3*2^3 => 8 threes

we remained with 28-4
- repeat the above process for 

"""


class Solution:
    def divide(self, dividend: int, divisor: int):
        # Special case: overflow
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # handle negatives
        is_neg = False
        if divisor < 0:
            divisor = abs(divisor)
            is_neg = not is_neg
        if dividend < 0:
            dividend = abs(dividend)
            is_neg = not is_neg

        # # actual division
        result = 0  # quotient
        while dividend >= divisor:
            curr_divisor = divisor
            two_power = 0

            while curr_divisor+curr_divisor <= dividend:
                curr_divisor += curr_divisor  # curr_divisor *= 2
                two_power += 1

            result += 2**two_power
            dividend -= curr_divisor

        if is_neg:
            return -result
        return result
