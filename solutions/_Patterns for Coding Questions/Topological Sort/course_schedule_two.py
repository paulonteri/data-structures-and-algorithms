"""
Course Schedule II:

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:
    Input: numCourses = 1, prerequisites = []
    Output: [0]

https://leetcode.com/problems/course-schedule-ii/
"""

import collections
"""
# indegree = count of incoming edges of each vertex/node or how many parents it has (used to determine sources)
# source: Any node that has no incoming edge and has only outgoing edges is called a source (indegree==0)

- top_sort = []
- get the topological sort of the courses
    - initialization:
        - create an adjacency list from the edge list given
        - while doing so, create an indegree record for each vertex/node
        - add all the sources into a queue
    - while queue:
        - get the element at the top of the queue (curr)
            - add it to the output
            - reduce the indegree for all of its children by one
                - if any child has an indegree of one after that, add it to the queue

- if the length of the sorted list == numCourses, it is possible to complete the courses, it is an asyclic graph 
"""


# import collections
class Solution:

    def findOrder(self, numCourses, prerequisites):

        top_sort = []

        # # create an adjacency list from the edge list given
        # while doing so, create an indegree record for each vertex/node
        adjacency_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for arr in prerequisites:
            child, parent = arr[0], arr[1]

            adjacency_list[parent].append(child)
            indegrees[child] += 1

        # # add all the sources into a queue
        queue = []
        for vertex in range(numCourses):
            if indegrees[vertex] == 0:
                queue.append(vertex)

        # # build top_sort list
        while queue:
            vertex = queue.pop(0)
            top_sort.append(vertex)
            for child in adjacency_list[vertex]:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append(child)

        # if the length of the sorted list == numCourses, it is possible to complete the courses
        if len(top_sort) == numCourses:
            return top_sort
        return []
