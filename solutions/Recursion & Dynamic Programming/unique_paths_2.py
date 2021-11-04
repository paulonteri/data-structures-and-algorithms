"""
Unique Paths II / Robot in Grid:

A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.

https://leetcode.com/problems/unique-paths-ii/
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
            return 0

        return self.helper(obstacleGrid)

    def helper(self, obstacleGrid,  row=0, col=0):
        # out of bounds
        if row >= len(obstacleGrid) or col >= len(obstacleGrid[0]):
            return 0
        # reached end
        elif row == len(obstacleGrid)-1 and col == len(obstacleGrid[0])-1:
            return 1
        # is occupied with obstacle
        elif obstacleGrid[row][col] == 1:
            return 0
        # get cached result
        elif obstacleGrid[row][col] < 0:
            return -obstacleGrid[row][col]

        # move right
        right = self.helper(obstacleGrid,  row, col+1)
        # move down
        down = self.helper(obstacleGrid,  row+1, col)

        obstacleGrid[row][col] = -(right + down)  # cache results

        return right + down
