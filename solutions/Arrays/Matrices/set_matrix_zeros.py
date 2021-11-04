"""
Set Matrix Zeroes:

Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Example 1:
    Input: matrix =
        [
        [1,1,1],
        [1,0,1],
        [1,1,1]]
    Output:
        [
        [1,0,1],
        [0,0,0],
        [1,0,1]
        ]
Example 2:
    Input: matrix =
    [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
    Output:
    [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
    ]

# Input: valid matrix
# Output: None
# Constraints:
    - edit array in-place

https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix):
        flag = "&"

        # # Find Matrix Zeroes
        first_col = first_row = False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:

                    # mark first row and col to be erased
                    matrix[row][0] = flag  # mark first col of row
                    matrix[0][col] = flag  # mark first row of col

                    if col == 0:
                        first_col = True
                    if row == 0:
                        first_row = True

        # # Set Matrix Zeroes
        # # do not set matrix zeros for the first row & column as they are used as guides for marking
        # deal with rows
        for row in range(1, len(matrix)):
            if matrix[row][0] == flag:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
        # deal with cols
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == flag:
                for row in range(len(matrix)):
                    matrix[row][col] = 0

        # # Set Matrix Zeroes for the first row & col
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        return matrix
