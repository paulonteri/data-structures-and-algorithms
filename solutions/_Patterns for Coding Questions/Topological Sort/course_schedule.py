"""
Course Schedule/Tasks Scheduling:
Course Schedule II is a prerequisite to this.

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.
Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
Example 3:
    Input: numCourses = 3, prerequisites=[0, 1], [1, 2]
    Output: true
    Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs 
            to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2] 
Example 4:
    Input: numCourses = 3, prerequisites=[0, 1], [1, 2], [2, 0]
    Output: false
    Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.
Example 5:
    Input: numCourses = 6, prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    Output: true
    Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]

https://leetcode.com/problems/course-schedule/
"""


"""
SOLUTION:

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
                
- return len(top_sort) == len(adjacency_list)
    - if len(top_sort) == len(adjacency_list), it means the graph is acyclic
"""




import collections
class Solution:
    def topSort(self, edge_list):
        top_sort = []

        # # create an adjacency list from the edge list given
        # while doing so, create an indegree record for each vertex/node
        adjacency_list = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for arr in edge_list:
            child, parent = arr[0], arr[1]

            adjacency_list[parent].append(child)
            indegrees[child] += 1

        # # add all the sources into a queue
        queue = []
        for vertex in adjacency_list:
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

        # if len(top_sort) == len(adjacency_list), it means the graph is acyclic
        return len(top_sort) == len(adjacency_list)

    def canFinish(self, numCourses, prerequisites):
        return self.topSort(prerequisites)


# ------------------------------------------------------------------------------------------------------------------------------------------------


class SolutionDFS:
    def dfs(self, adjacency_list, visited_cache, vertex, curr_visiting):
        if vertex in visited_cache:
            return True
        if vertex in curr_visiting:
            return False

        curr_visiting.add(vertex)
        for child in adjacency_list[vertex]:
            if not self.dfs(adjacency_list, visited_cache, child, curr_visiting):
                return False
        curr_visiting.remove(vertex)

        visited_cache.add(vertex)
        return True

    def canFinish(self, numCourses, prerequisites):

        # # create an adjacency list from the edge list given
        adjacency_list = collections.defaultdict(list)
        for arr in prerequisites:
            child, parent = arr[0], arr[1]
            adjacency_list[parent].append(child)

        visited_cache = set()
        for vertex in list(adjacency_list.keys()):
            if not self.dfs(adjacency_list, visited_cache, vertex, set()):
                return False

        return True
