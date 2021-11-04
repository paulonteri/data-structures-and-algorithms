""" 
Multiply Strings:

Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"
Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

https://leetcode.com/problems/multiply-strings
"""


class Solution:
    def multiply(self, num1: str, num2: str):
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0] * (len(num1) + len(num2))

        for i_one in reversed(range(len(num1))):
            for i_two in reversed(range(len(num2))):
                # +1 is used to handle (0,0) i_one=0 i_two=0 carries
                # placing their carry will be easier if we move every element one step back/ to the right
                pos = i_one + i_two + 1

                carry = res[pos]
                multiplication = (int(num1[i_one]) * int(num2[i_two])) + carry

                # save
                res[pos] = multiplication % 10
                # place carry
                res[pos-1] += multiplication // 10

        # remove leading zeros
        idx = 0
        while res[idx] == 0:
            idx += 1
        res = res[idx:]

        # return answer
        return "".join([str(num) for num in res])
