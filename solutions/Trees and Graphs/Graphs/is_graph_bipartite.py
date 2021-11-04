""" 
785. Is Graph Bipartite?

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. 
You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. 
More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:
    There are no self-edges (graph[u] does not contain u).
    There are no parallel edges (graph[u] does not contain duplicate values).
    If v is in graph[u], then u is in graph[v] (the graph is undirected).
    The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets 
 A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

https://leetcode.com/problems/is-graph-bipartite
https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#dc05cd22189b412f8a0a8c1d1a827bde
"""


class Solution:
    def isBipartite(self, graph):

        colours = [None] * len(graph)
        visited = [False] * len(graph)

        for node in range(len(graph)):
            if not self.dfs(graph, node, colours, visited):
                return False
        return True

    def dfs(self, graph, node, colours, visited):
        if visited[node]:
            return True
        if colours[node] is None:
            # https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#596387a8e4254e1690f5eca7996ab9a1
            # if we do not know the colour then we can group it with the nodes in which we do not know the colours
            colours[node] = True

        visited[node] = True

        # Check colours & Dfs
        for child in graph[node]:
            if colours[child] is None:
                colours[child] = not colours[node]
            # check for correct colours
            if colours[child] == colours[node]:
                return False

            # Dfs
            if not self.dfs(graph, child, colours, visited):
                return False

        return True
