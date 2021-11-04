""" 
Path With Maximum Minimum Value:

Given an m x n integer matrix grid, 
    return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.
The score of a path is the minimum value in that path.
For example, the score of the path 8 → 4 → 5 → 9 is 4.

Example 1:
    Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
    Output: 4
    Explanation: The path with the maximum score is highlighted in yellow. 
Example 2:
    Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
    Output: 2
Example 3:
    Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
    Output: 3

https://leetcode.com/problems/path-with-maximum-minimum-value/
https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/457525/JAVA-A-Summery-of-All-Current-Solutions
https://www.notion.so/paulonteri/Heaps-Priority-Queues-bb4a8de1dbe54089854d8d03c833126c#a8a0e9b8526c4b42a37090b4df52ed3a
"""

import heapq

""" 
To prune our search tree, we take a detailed look at our problem. 
Since we have no need to find the shortest path, we could only focus on how to find a path avoiding small values. 
To do so, we could sort adjacents of our current visited vertices to find the maximum, 
    and always choose the maximum as our next step. 
To implement, we could use a heap to help us maintaining all adjacents and the top of the heap is the next candidate.

Time: O(Vlog(V) + E). Because the maximum number of element in the queue cannot be larger than V so pushing and popping from queue is O(log(V)). 
    Also we only push each vertex to the queue once, so at maximum we do it V times. Thats Vlog(V). The E bit comes from the for loop inside the while loop.
Space: O(V) where V is the maximum depth of our search tree.

Uses: reversed Prim's Minimum Spanning Tree Algorithm
https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#596bc798759a4edabe22a895aadeb12c
"""


class Solution(object):
    def maximumMinimumPath(self, A):
        """
        ensure we always visit the larger neighbours 
        the max_heap will ensure that the smallest neighbours are not visited

        Even if we took a wrong path, we can always take the right path again 
            because the max_heap will return us to the next valid large spot/neighbour
        """
        DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        maxscore = A[0][0]
        max_heap = []
        # negate element to simulate max heap
        heapq.heappush(max_heap, (-A[0][0], 0, 0))

        while len(max_heap) != 0:
            val, row, col = heapq.heappop(max_heap)

            # update max
            maxscore = min(maxscore, -val)

            # reached last node
            if row == len(A) - 1 and col == len(A[0]) - 1:
                break

            for d in DIRS:
                new_row, new_col = d[0] + row, d[1] + col

                is_valid_row = new_row >= 0 and new_row < len(A)
                is_valid_col = new_col >= 0 and new_col < len(A[0])
                if is_valid_row and is_valid_col and A[new_row][new_col] >= 0:
                    heapq.heappush(
                        max_heap, (-A[new_row][new_col], new_row, new_col)
                    )
                    # mark as visited
                    A[new_row][new_col] = -1

        return maxscore
