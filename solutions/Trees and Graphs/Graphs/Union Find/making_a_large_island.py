""" 
Making A Large Island

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.

Example 1:
    Input: grid = [[1,0],[0,1]]
    Output: 3
    Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:
    Input: grid = [[1,1],[1,0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:
    Input: grid = [[1,1],[1,1]]
    Output: 4
    Explanation: Can't change any 0 to 1, only one island with area = 4.


https://leetcode.com/problems/making-a-large-island
"""
from collections import defaultdict
from typing import List


# O(N^4) time | O(N^2) space
# we traverse the graph twice in the worst case, for time, and only store row*col nodes, for space
class Solution:
    def largestIsland(self, grid: List[List[int]]):
        """ 
        * Based on union find: https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#02cd6da5a64447feab03037d22d40b38

        - Group nodes into different islands
            - store the island sizes
        - For each 0, try to merge its sorrounding islands
        """
        island_size, child_to_island = self.create_islands(grid)
        largest_island = 0
        if island_size:
            largest_island = max(island_size.values())

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    continue
                seen_islands = set()

                top_island, top = self.get_nodes_island_size(
                    grid, row-1, col, island_size, child_to_island)
                seen_islands.add(top_island)

                bottom_island, bottom = self.get_nodes_island_size(
                    grid, row+1, col, island_size, child_to_island)
                # is part of an island we saw above (in this case part of top_island)
                if bottom_island in seen_islands:
                    bottom = 0
                seen_islands.add(bottom_island)

                left_island, left = self.get_nodes_island_size(
                    grid, row, col-1, island_size, child_to_island)
                # is part of an island we saw above (in this case part of top_island and/or bottom_island)
                if left_island in seen_islands:
                    left = 0
                seen_islands.add(left_island)

                right_island, right = self.get_nodes_island_size(
                    grid, row, col+1, island_size, child_to_island)
                if right_island in seen_islands:
                    right = 0
                seen_islands.add(right_island)

                # merge all neighbouring islands + the current node (1)
                largest_island = max(largest_island, 1+top+bottom+left+right)

        return largest_island

    def get_nodes_island_size(self, grid, row, col, island_size, child_to_island):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return None, 0
        if grid[row][col] == 0:
            return None, 0
        island = child_to_island[(row, col)]
        return island, island_size[island]

    def create_islands(self, grid: List[List[int]]):
        island_size = defaultdict(int)
        child_to_island = {}

        def dfs(row, col, island):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in child_to_island:
                return
            if grid[row][col] == 0:
                return

            island_size[island] += 1
            child_to_island[(row, col)] = island

            dfs(row-1, col, counter)
            dfs(row, col-1, counter)
            dfs(row+1, col, counter)
            dfs(row, col+1, counter)

        counter = -1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dfs(row, col, counter)
                counter -= 1

        return island_size, child_to_island
