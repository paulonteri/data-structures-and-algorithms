""" 
Max Area of Island:

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0
Example 3:
    [[1,1,0],[0,0,0]]
    2

https://leetcode.com/problems/max-area-of-island/
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        maximum = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1:
                    maximum = max(
                        maximum, self.areOfIsland(grid, row, col))

        return maximum

    def areOfIsland(self, grid, row, col):
        if not (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1):
            return 0

        grid[row][col] = 0  # remove

        count = 1

        # up
        count += self.areOfIsland(grid, row-1, col)
        # down
        count += self.areOfIsland(grid, row+1, col)
        # left
        count += self.areOfIsland(grid, row, col-1)
        # right
        count += self.areOfIsland(grid, row, col+1)

        return count
