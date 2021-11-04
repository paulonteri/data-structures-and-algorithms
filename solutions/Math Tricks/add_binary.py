""" 
Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"
Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

https://leetcode.com/problems/add-binary
"""


class Solution:
    def addBinary(self, a: str, b: str):
        n = max(len(a), len(b))
        res = [0]*(n+1)

        one_idx = len(a)-1
        two_idx = len(b)-1
        for idx in reversed(range(n+1)):
            carry = res[idx]
            one = 0
            two = 0
            if one_idx >= 0:
                one = int(a[one_idx])
                one_idx -= 1
            if two_idx >= 0:
                two = int(b[two_idx])
                two_idx -= 1

            addition = one + two + carry

            res[idx] = addition % 2  # save result
            # save carry
            if addition // 2:  # prevent saving carry in idx 0
                res[idx-1] = addition // 2

        # remove preceeding zeros
        start_idx = 0
        while res[start_idx] == 0 and start_idx < len(res)-1:
            start_idx += 1
        res = res[start_idx:]

        return "".join([str(item) for item in res])
