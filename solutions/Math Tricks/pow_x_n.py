""" 
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000
Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100
Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

https://leetcode.com/problems/powx-n
https://youtu.be/g9YQyYi4IQQ
"""

""" 
2 ** 6
2*2*2*2*2*2
2**3 * 2**3
(2**2 * 2**1) * (2**2 * 2**1)
(2**1 * 2**1 * 2**1) * (2**1 * 2**1 * 2**1)

2^12 => (2^6)^2
2^6  => (2^3)^2
2^3  => (2^1)^2 * 2

2^10 => (2^5)^2
2^5  => (2^2)^2 * 2
2^2  => (2^1)^2
"""


class Solution:
    def myPow(self, x: float, n: int):
        res = self.my_pow_helper(x, abs(n))

        if n < 0:
            return 1/res
        return res

    def my_pow_helper(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x

        half_n = n // 2
        n_is_odd = n % 2 != 0

        # calculate power
        half_power = self.my_pow_helper(x, half_n)

        if n_is_odd:
            return half_power * half_power * x
        return half_power * half_power
