""" 
Connecting Cities With Minimum Cost

There are n cities labelled from 1 to n. 
You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.
Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,
The cost is the sum of the connections' costs used.

Example 1:
    Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
    Output: 6
    Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:
    Input: n = 4, connections = [[1,2,3],[3,4,4]]
    Output: -1
    Explanation: There is no way to connect all cities even if all edges are used.

https://leetcode.com/problems/connecting-cities-with-minimum-cost/
https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#127f401fa2624fbebe9ea79bc7fad235
"""

import collections
import heapq

""" 
Prim's Minimum Spanning Tree Algorithm: https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#596bc798759a4edabe22a895aadeb12c
"""


class Solution:
    def minimumCost(self, n: int, connections):
        total_cost = 0

        # # Create adjacency list
        # Will store  nodes in the form => `parent: [[cost_to_1, node_1], [cost_to_2, node_2], ...]`
        graph = collections.defaultdict(set)
        for city_x, city_y, cost in connections:
            graph[city_x].add((cost, city_y))
            graph[city_y].add((cost, city_x))

        # # Prim's Minimum Spanning Tree Algorithm
        visited = set()
        priority_queue = []
        heapq.heappush(priority_queue, (0, 1))  # start from node 1
        while priority_queue:
            cost, node = heapq.heappop(priority_queue)
            # skip visited
            if node in visited:
                continue
            visited.add(node)

            total_cost += cost
            for neighbour_cost, neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(priority_queue, [neighbour_cost, neighbour])

        if len(visited) == n:
            return total_cost
        return -1
