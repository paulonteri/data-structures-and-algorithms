""" 
Unique Paths:

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example 1:
    Input: m = 3, n = 7
    Output: 28
Example 2:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down
Example 3:
    Input: m = 7, n = 3
    Output: 28
Example 4:
    Input: m = 3, n = 3
    Output: 6
Example:
		99*1 => 1
Example
	99*2 => 99

Number Of Ways To Traverse Graph:
You're given two positive integers representing the width and height of a grid-shaped, rectangular graph.
Write a function that returns the number of ways to reach the bottom right corner of the graph when starting at the top left corner.
Each move you take must either go down or right. In other words, you can never move up or left in the graph.
For example, given the graph illustrated below, with width = 2 and height = 3, 
    there are three ways to reach the bottom right corner when starting at the top left corner:
        _ _
        |_|_|
        |_|_|
        |_|_|
        Down, Down, Right
        Right, Down, Down
        Down, Right, Down
Note: you may assume that width * height >= 2.
In other words, the graph will never be a 1x1 grid.
    Sample Input
    width = 4
    height = 3
    Sample Output
    10

https://leetcode.com/problems/unique-paths
https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Traverse%20Graph
https://www.notion.so/paulonteri/Recursion-DP-Backtracking-525dddcdd0874ed98372518724fc8753#f980e95403a24443a371a10430a198ad

Unique Paths II can help in understanding this
"""

"""
Since robot can move either down or right, 
	there is only one path to reach the cells in the first row: right->right->...->right.
	The same is valid for the first column, though the path here is down->down-> ...->down.
"""


# starting from end to beginning
# note that the start is 1,1. 0,0 is out of bounds
class SolutionMEMO:
    def uniquePaths(self, m, n):
        cache = [[False for _ in range(n+1)] for _ in range(m+1)]
        return self.uniquePathsHelper(m, n, cache)

    def uniquePathsHelper(self, m, n, cache):
        if m == 1 and n == 1:
            return 1
        if m < 1 or n < 1:
            return float('-inf')
        if cache[m][n]:
            return cache[m][n]

        left = self.uniquePathsHelper(m, n-1, cache)
        up = self.uniquePathsHelper(m-1, n, cache)

        total = 0
        if left != float('-inf'):
            total += left
        if up != float('-inf'):
            total += up

        cache[m][n] = total
        return cache[m][n]


""" 
-------------------------------------------------------------------------------------------------------------------------------------

what if the graph was:
[
  1
1[1],
]

[
  1  2
1[1, 1],
2[1, 2],
]

[
  1  2  3
1[1, 1, 1],
2[1, 2, 3],
3[1, 3, 6]
]


[
  1  2  3  4
1[1, 1, 1, 1],
2[1, 2, 3, 4],
3[1, 3, 6, 10],
4[1, 4, 10, 20]
]

"""


class Solution:
    def uniquePaths(self, m, n):
        if m == 1 and n == 1:
            return 1
        cache = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # fill in defaults
        for i in range(1, n+1):
            cache[1][i] = 1
        for i in range(1, m+1):
            cache[i][1] = 1

        for h in range(2, m+1):
            for w in range(2, n+1):
                #                      top  +  left
                cache[h][w] = cache[h-1][w] + cache[h][w-1]

        # print(cache)
        return cache[-1][-1]
