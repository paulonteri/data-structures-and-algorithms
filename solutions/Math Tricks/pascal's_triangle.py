""" 
Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
    Input: numRows = 1
    Output: [[1]]

https://leetcode.com/problems/pascals-triangle
"""


class Solution:
    def generate(self, numRows: int):
        triangle = []
        if numRows < 1:
            return triangle

        # add the first row
        triangle.append([1])

        for i in range(1, numRows):  # start with 2nd row
            row = []

            # we handle the first and last indices separately
            row.append(1)  # first index

            # items to calculate/add will always be equal to the index (i) - 1
            # for example in the 4th row (i=3) we calculate 2 values
            for x in range(1, i):
                # we know that each character is the sum of those above it: above left and above right
                row.append(triangle[i-1][x-1] + triangle[i-1][x])

            row.append(1)  # last index for row

            triangle.append(row)

        return triangle
