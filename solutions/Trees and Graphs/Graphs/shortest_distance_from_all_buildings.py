""" 
Shortest Distance from All Buildings

You are given an m x n grid grid of values 0, 1, or 2, where:
    each 0 marks an empty land that you can pass by freely,
    each 1 marks a building that you cannot pass through, and
    each 2 marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. 
You can only move up, down, left, and right.

Return the shortest travel distance for such a house. 
If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example 1:
    Input: 
        grid = 
        [
            [1,0,2,0,1],
            [0,0,0,0,0],
            [0,0,1,0,0]
        ]
    Output: 
        7
    Explanation: 
        Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
        The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
        So return 7.
Example 2:
    Input: grid = [[1,0]]
    Output: 1
Example 3:
    Input: grid = [[1]]
    Output: -1
    
https://leetcode.com/problems/shortest-distance-from-all-buildings
https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#60f4275d6bd946cf88c5b50f2db06deb
"""

""" 
1. BFS from free space to all houses
2. BFS from houses to free spaces 

"""


# Let N and M be the number of rows and columns in grid respectively.
# O(N^2 . M^2) time | O(N . M) time
class Solution:
    def shortestDistance(self, grid):
        """ 
        BFS from Houses to Empty Land
        """
        houses_reached = [
            [0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        # # count houses
        houses_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    houses_count += 1

        # # bfs on each house
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # check if house
                if grid[row][col] == 1:
                    self.bfs(row, col, grid, houses_reached)

        # # find suitable free space
        largest = float('-inf')
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # check if valid free space
                if houses_reached[row][col] == houses_count and grid[row][col] < 0:
                    largest = max(largest, grid[row][col])

        if largest == float('-inf'):
            return -1
        return largest * -1

    def bfs(self, row, col, grid, houses_reached):
        visited = [
            [False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = []

        # initialise queue
        queue.append((row-1, col, -1))
        queue.append((row+1, col, -1))
        queue.append((row, col-1, -1))
        queue.append((row, col+1, -1))

        while queue:
            c_row, c_col, distance = queue.pop(0)
            if c_row < 0 or c_row >= len(grid):
                continue
            if c_col < 0 or c_col >= len(grid[0]):
                continue
            if visited[c_row][c_col]:
                continue
            if grid[c_row][c_col] > 0:
                continue

            visited[c_row][c_col] = True

            # # record distance
            grid[c_row][c_col] += distance
            houses_reached[c_row][c_col] += 1

            # # move outward
            new_distance = distance - 1
            queue.append((c_row-1, c_col, new_distance))
            queue.append((c_row+1, c_col, new_distance))
            queue.append((c_row, c_col-1, new_distance))
            queue.append((c_row, c_col+1, new_distance))
