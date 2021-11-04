""" 
Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
Example 2:
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

https://leetcode.com/problems/rotting-oranges
"""

from typing import List
import collections

""" 
BFS
One of the most distinguished code patterns in BFS algorithms is that often we use a queue data structure to keep track of the candidates that we need to visit during the process.

The main algorithm is built around a loop iterating through the queue. At each iteration, we pop out an element from the head of the queue. 
Then we do some particular process with the popped element. More importantly, we then append neighbors of the popped element into the queue, to keep the BFS process running.

O(N) time | O(N) space
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        minutes_needed = 0

        rotten = collections.deque()

        # # scan the grid to find the initial values for the queue
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten.append((row, col))

        # # run the BFS process on the queue,
        while rotten:
            found_fresh = False

            # empty rotten queue
            for _ in range(len(rotten)):
                rotten_row, rotten_col = rotten.popleft()
                for row, col in self.get_neighbours(grid, rotten_row, rotten_col):
                    # if fresh
                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        rotten.append((row, col))
                        found_fresh = True

            if found_fresh:
                minutes_needed += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1

        return minutes_needed

    def get_neighbours(self, grid, row, col):
        neighbours = []
        if row-1 >= 0:
            neighbours.append((row-1, col))
        if row+1 < len(grid):
            neighbours.append((row+1, col))
        if col-1 >= 0:
            neighbours.append((row, col-1))
        if col+1 < len(grid[0]):
            neighbours.append((row, col+1))
        return neighbours
