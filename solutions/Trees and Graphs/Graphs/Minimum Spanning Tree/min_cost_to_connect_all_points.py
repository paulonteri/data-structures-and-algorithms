""" 
1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
    Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    Output: 20
Explanation:
    We can connect the points as shown above to get the minimum cost of 20.
    Notice that there is a unique path between every pair of points.
Example 2:
    Input: points = [[3,12],[-2,5],[-4,1]]
    Output: 18
Example 3:
    Input: points = [[0,0],[1,1],[1,0],[-1,1]]
    Output: 4
Example 4:
    Input: points = [[-1000000,-1000000],[1000000,1000000]]
    Output: 4000000
Example 5:
    Input: points = [[0,0]]
    Output: 0

https://leetcode.com/problems/min-cost-to-connect-all-points
https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#2ac2c79816464704a3851de16d494dff
"""

import collections
import heapq

""" 
Prim's Minimum Spanning Tree Algorithm: https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#596bc798759a4edabe22a895aadeb12c
https://youtu.be/f7JOBJIC-NA
"""


class Solution_:
    def minCostConnectPoints(self, points):
        total = 0

        # # Create adjacency list
        # Will store  nodes in the form => `parent: [[cost_to_1, node_1], [cost_to_2, node_2], ...]`
        graph = collections.defaultdict(list)
        for idx in range(len(points)):
            x1, y1 = points[idx]
            for idx2 in range(idx + 1, len(points)):
                x2, y2 = points[idx2]
                cost = abs(x1 - x2) + abs(y1 - y2)

                graph[str(x1)+str(y1)].append([cost, str(x2)+str(y2)])
                graph[str(x2)+str(y2)].append([cost, str(x1)+str(y1)])

        # # Prim's Minimum Spanning Tree Algorithm
        visited = set()
        priority_queue = []
        first_node = str(points[0][0])+str(points[0][1])
        heapq.heappush(priority_queue, (0, first_node))  # start from node 0
        while len(visited) < len(graph):
            cost, node = heapq.heappop(priority_queue)
            # skip visited
            if node in visited:
                continue
            visited.add(node)

            # record cost
            total += cost
            # add neighbours
            for neighbour in graph[node]:
                if neighbour[1] not in visited:
                    heapq.heappush(priority_queue, neighbour)

        return total


class Solution:
    def minCostConnectPoints(self, points):

        total = 0

        # # Create adjacency list
        # Will use the array indices as id's
        # Will store  nodes in the form => `parent: [[cost_to_1, node_1], [cost_to_2, node_2], ...]`
        graph = collections.defaultdict(list)
        for idx in range(len(points)):
            x1, y1 = points[idx]
            for idx2 in range(idx + 1, len(points)):
                x2, y2 = points[idx2]
                cost = abs(x1 - x2) + abs(y1 - y2)

                graph[idx].append([cost, idx2])
                graph[idx2].append([cost, idx])

        # # Prim's Minimum Spanning Tree Algorithm
        visited = set()
        priority_queue = []
        heapq.heappush(priority_queue, (0, 0))  # start from node 0
        while len(visited) < len(graph):
            cost, node = heapq.heappop(priority_queue)
            # skip visited
            if node in visited:
                continue
            visited.add(node)

            # record cost
            total += cost
            # add neighbours
            for neighbour in graph[node]:
                if neighbour[1] not in visited:
                    heapq.heappush(priority_queue, neighbour)

        return total
