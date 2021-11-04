""" 
Strobogrammatic Number II

Given an integer n, return all the strobogrammatic numbers that are of length n. 
You may return the answer in any order.
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:
    Input: n = 2
    Output: ["11","69","88","96"]
Example 2:
    Input: n = 1
    Output: ["0","1","8"]

https://leetcode.com/problems/strobogrammatic-number-ii
"""


""" 
We realised that we have 2 base cases (simplest subproblems):
    - n=1  --> ['0', '1', '8']
    - n=2  --> ['00', '11', '88', '69', '96']
The rest can be built around that:
    - n=3  
        -->               ["101","808","609","906","111","818","619","916","181","888","689","986"] 
        all w invalid --> ["000","101","808","609","906","010","111","818","619","916","080","181","888","689","986"]
    - n=4  
        -->               ["1001","8008","6009","9006","1111","8118","6119","9116","1881","8888","6889","9886","1691","8698","6699","9696","1961","8968","6969","9966"]
        all w invalid --> ["0000","1001","8008","6009","9006","0110","1111","8118","6119","9116","0880","1881","8888","6889","9886","0690","1691","8698","6699","9696","0960","1961","8968","6969","9966"]


Have a recursive function that builds from the base cases upwards:
Example:
    ```
    def helper(n):
        if n == 1:
            return ['0', '1', '8']
        if n == 2:
            return ['00', '11', '88', '69', '96']
        result = []

        for base in helper(n-2):
            result.append('0' + base + '0')
            result.append('1' + base + '1')
            result.append('6' + base + '9')
            result.append('8' + base + '8')
            result.append('9' + base + '6')

        return result
    ```
then return the valid results
"""


class Solution_:
    def findStrobogrammatic(self, n: int):
        result = []

        for num in self.findStrobogrammatic_helper(n):
            # remove leading zeros
            if str(int(num)) == num:
                result.append(num)

        return result

    def findStrobogrammatic_helper(self, n):
        # Base cases
        if n == 1:
            return ['0', '1', '8']
        if n == 2:
            return ['00', '11', '88', '69', '96']
        result = []

        # this is the only way they can be expanded
        for base in self.findStrobogrammatic_helper(n-2):
            result.append('0' + base + '0')
            result.append('1' + base + '1')
            result.append('6' + base + '9')
            result.append('8' + base + '8')
            result.append('9' + base + '6')

        return result


# Time complexity O(n). We iterate n//2 times in for _ in range(n//2). Within this, we iterate for num in output at most 5 times, since output has at most 5 numbers.
# Space complexity O(n).
class Solution:
    def findStrobogrammatic(self, n: int):
        result = []

        # handle even or odd
        combinations = [''] if n % 2 == 0 else ['0', '1', '8']
        for _ in range(n//2):
            temp = []
            for num in combinations:
                temp.append('0' + num + '0')
                temp.append('1' + num + '1')
                temp.append('8' + num + '8')
                temp.append('6' + num + '9')
                temp.append('9' + num + '6')
            combinations = temp

        for num in combinations:
            # remove leading zeros
            if str(int(num)) == num:
                result.append(num)

        return result
