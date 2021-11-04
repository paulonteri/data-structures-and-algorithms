"""
Search a 2D Matrix:

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

https://leetcode.com/problems/search-a-2d-matrix/
"""
from typing import List
"""
Search In Sorted Matrix:

You're given a two-dimensional array (a matrix) of distinct integers and a target integer.
Each row in the matrix is sorted, and each column is also sorted; the matrix doesn't necessarily have the same height and width.
Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise [-1, -1].

Sample Input:
    matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
    ]
    target = 44
Sample Output:
    [3, 3]
    
https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix
"""


class Solution0:
    def binarySearch(self, target, array):
        left = 0
        right = len(array)-1
        while left <= right:
            mid = (right + left) // 2

            if array[mid] == target:
                return True
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int):

        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                return self.binarySearch(target, row)

        return False


""" 
matrix = 
[
    [1,  3, 5, 7],
    [10,11,16,20],
    [23,30,34,60]
]

target = 13
Output: false

target = 16
Output: true

target = 16
---
if we start at 0,0
    - we do not know if it is in current row, or those below
---
if we start at 0,4
    - we are sure it isn't in current row, we move down
        - at  1,4:
            - we are sure it is in this row or none other
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):

        row = 0
        while row < len(matrix):

            # # check rows
            # check last item in row
            if matrix[row][len(matrix[0])-1] < target:  # move to next row
                row += 1
            elif matrix[row][0] > target:
                return False

            # # found correct row
            # Binary Search on Row
            else:
                left = 0
                right = len(matrix[0])-1
                while left <= right:

                    mid = (right + left) // 2

                    if matrix[row][mid] == target:
                        return True

                    if matrix[row][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1

                return False

        return False


def searchInSortedMatrix(matrix, target):

    # start at top right
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1  # move left
        elif matrix[row][col] < target:
            row += 1  # move down
        else:
            return[row, col]

    return[-1, -1]


"""

matrix = [
  [1, 4, 7, 12, 15, 1000],
  [2, 5, 19, 31, 32, 1001],
  [3, 8, 24, 33, 35, 1002],
  [40, 41, 42, 44, 45, 1003],
  [99, 100, 103, 106, 128, 1004],
]
target = 44

- Start curr at the top right corner
- Check wether you should increase or decrease curr's value
	Move sideways(decrease), downwards (increase)
- 

"""
