""" 
Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:
    NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

Example 1:
    Input
        ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
    Output
        [null, 8, 11, 12]
    Explanation
        NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
        numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
        numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
        numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -105 <= matrix[i][j] <= 105
    0 <= row1 <= row2 < m
    0 <= col1 <= col2 < n
    At most 104 calls will be made to sumRegion.

https://leetcode.com/problems/range-sum-query-2d-immutable
    https://www.notion.so/paulonteri/Object-Oriented-Analysis-and-Design-1a01887a9271475da7b3cd3f4efc9e0d#4925b17f4f7142b88467b45d66602384
"""


class NumMatrix:
    """ 
    Pre-compute the cumulative sums for each row to give O(R) lookup 
    where R in the number of rows requested
    """

    def __init__(self, matrix):
        self.row_sums = [
            [0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))
        ]

        for row_idx in range(len(matrix)):
            running_sum = 0
            for col_idx, num in enumerate(matrix[row_idx]):
                running_sum += num
                self.row_sums[row_idx][col_idx] = running_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        total = 0

        for row_idx in range(row1, row2+1):
            total += self._get_row_sum(self.row_sums[row_idx], col1, col2)

        return total

    def _get_row_sum(self, row, left, right):
        left_val = 0
        if left > 0:
            left_val = row[left-1]
        return row[right] - left_val


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

""" 

"""


class NumMatrix2:
    """ 
    Here we use the technique of integral image, which is introduced to speed up block computation.
    https://www.notion.so/paulonteri/Object-Oriented-Analysis-and-Design-1a01887a9271475da7b3cd3f4efc9e0d#4925b17f4f7142b88467b45d66602384
    """

    def __init__(self, matrix):

        # build integral image by recurrence relationship
        self.integral_image = [
            [0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))
        ]

        for row in range(len(matrix)):

            running_sum = 0
            for col in range(len(matrix[0])):
                running_sum += matrix[row][col]
                self.integral_image[row][col] = running_sum
                # add top row
                if row > 0:
                    self.integral_image[row][col] += self.integral_image[row-1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):

        bottom_right = self.integral_image[row2][col2]
        #
        bottom_left = 0
        if col1 > 0:
            bottom_left = self.integral_image[row2][col1-1]
        #
        top_right = 0
        if row1 > 0:
            top_right = self.integral_image[row1-1][col2]
        #
        top_left = 0
        if col1 > 0 and row1 > 0:
            top_left = self.integral_image[row1 - 1][col1-1]

        # calculate area
        return bottom_right - bottom_left - top_right + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
