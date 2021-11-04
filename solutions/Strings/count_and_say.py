""" 
Count and Say:

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
    Input: n = 1
    Output: "1"
    Explanation: This is the base case.
Example 2:
    Input: n = 4
    Output: "1211"
    Explanation:
        countAndSay(1) = "1"
        countAndSay(2) = say "1" = one 1 = "11"
        countAndSay(3) = say "11" = two 1's = "21"
        countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

https://leetcode.com/problems/count-and-say
"""


class Solution:
    def countAndSay(self, n: int):
        if n == 1:
            return '1'

        res = [1]
        for _ in range(n-1):
            new_res = []

            curr = res[0]
            count = 1
            for idx in range(1, len(res)):
                if res[idx] == curr:
                    count += 1
                else:
                    new_res.append(count)
                    new_res.append(curr)
                    # reset
                    curr = res[idx]
                    count = 1

            new_res.append(count)
            new_res.append(curr)

            res = new_res

        return "".join([str(num) for num in res])
