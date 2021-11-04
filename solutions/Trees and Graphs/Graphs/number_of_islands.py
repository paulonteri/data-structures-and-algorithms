""" 
Number of Islands:

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
    Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    Output: 1
Example 2:
    Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    Output: 3

https://leetcode.com/problems/number-of-islands/
"""


class Solution:
    def numIslands(self, grid):
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1":
                    count += 1
                    self.removeOneIsland(grid, row, col)

        return count

    def removeOneIsland(self, grid, row, col):
        if not (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == "1"):
            return

        grid[row][col] = "0"  # remove

        # up
        self.removeOneIsland(grid, row-1, col)
        # down
        self.removeOneIsland(grid, row+1, col)
        # left
        self.removeOneIsland(grid, row, col-1)
        # right
        self.removeOneIsland(grid, row, col+1)
