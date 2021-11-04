""" 
Cheapest Flights Within K Stops

There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
    Output: 200
    Explanation: The graph is shown.
    The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
    Output: 500
    Explanation: The graph is shown.
    The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

https://leetcode.com/problems/cheapest-flights-within-k-stops
"""

import collections
import heapq


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        # Build graph
        graph = collections.defaultdict(list)
        for from_node, to_node, price in flights:
            graph[from_node].append((price, to_node))

        # Dijkstra's Algorithm
        heap = [(0, src, 0)]  # price, city, stops
        visited = set()
        city_stops = [float('inf')] * n  # shortest distance/price to node
        while heap:
            price, city, stops = heapq.heappop(heap)

            if city == dst:
                return price
            if stops == k+1:
                continue
            # # Note: in Dijkstra's Algorithm, we never revisit nodes
            # Remember that our algorithm stops whenever we pass k stops/visits - we need to consider this & look for a path that will give us less stops
            # Therefore, if we ever encounter a node that has already been processed before
            #   but the number of stops from the source is lesser than what was recorded before,
            #   we will add it to the heap so that it gets considered again!
            # That's the only change we need to make to make Dijkstra's compliant with the limitation on the number of stops.
            #   if city in visited:   <- normal Dijkstra's Algorithm
            #   if city in visited and stops > city_stops[city]:    <- modified Dijkstra's Algorithm
            if city in visited and stops > city_stops[city]:
                continue

            visited.add(city)
            city_stops[city] = stops

            for neighbour_cost, neighbour in graph[city]:
                heapq.heappush(
                    heap, (price+neighbour_cost,  neighbour, stops+1,)
                )

        return -1
