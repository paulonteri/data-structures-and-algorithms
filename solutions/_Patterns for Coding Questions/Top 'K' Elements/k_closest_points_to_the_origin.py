""" 
'K' Closest Points to the Origin:

Given an array of points in a 2D2D plane, find ‘K’ closest points to the origin.

Example 1:
    Input: points = [[1,2],[1,3]], K = 1
    Output: [[1,2]]
    Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
    The Euclidean distance between (1, 3) and the origin is sqrt(10).
    Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
Example 2:
    Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
    Output: [[1, 3], [2, -1]]

https://leetcode.com/problems/k-closest-points-to-origin
https://www.educative.io/courses/grokking-the-coding-interview/3YxNVYwNR5p
"""
""" 
The Euclidean distance of a point P(x,y) from the origin can be calculated through the following formula:
    math.sqrt(x^2 + y^2)
"""

# # Question
# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def print_point(self):
#         print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


# def find_closest_points(points, k):
#     result = []
#     return result




import heapq
import math
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for max-heap sorting
    # can also use less than __lt__
    def __gt__(self, other: 'Point'):
        # return self.distance_from_origin() > other.distance_from_origin()
        # we sort this way to ensure we have the k closest/smallest
        return self.distance_from_origin() < other.distance_from_origin()

    def distance_from_origin(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    result = []
    for point in points:
        heapq.heappush(result, point)
        while len(result) > k:
            heapq.heappop(result)

    return result
