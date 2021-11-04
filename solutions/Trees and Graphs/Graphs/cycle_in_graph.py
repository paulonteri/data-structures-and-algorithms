"""
Cycle In Graph:

You're given a list of edges representing an unweighted, directed graph with at least one node.
Write a function that returns a boolean representing whether the given graph contains a cycle.
For the purpose of this question, a cycle is defined as any number of vertices, including just one vertex, that are connected in a closed chain.
A cycle can also be defined as a chain of at least one vertex in which the first vertex is the same as the last.

The given list is what's called an adjacency list, and it represents a graph.
The number of vertices in the graph is equal to the length of edges, where each index i in edges contains vertex i's outbound edges, in no particular order.
Each individual edge is represented by a positive integer that denotes an index (a destination vertex) in the list that this vertex is connected to.
Note that these edges are directed, meaning that you can only travel from a particular vertex to its destination,
 not the other way around (unless the destination vertex itself has an outbound edge to the original vertex).
Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin;
 in other words, it's an edge that connects a vertex to itself. For the purpose of this question, a self-loop is considered a cycle.

Sample Input
    edges = [
    [1, 3],
    [2, 3, 4],
    [0],
    [],
    [2, 5],
    [],
    ]
Sample Output
    true 
    // There are multiple cycles in this graph: 
    // 1) 0 -> 1 -> 2 -> 0
    // 2) 0 -> 1 -> 4 -> 2 -> 0
    // 3) 1 -> 2 -> 0 -> 1
    // These are just 3 examples; there are more.

https://www.algoexpert.io/questions/Cycle%20In%20Graph
"""


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

def cycleInGraph0(edges):
    # # start dfs at each vertex -> loop can start anywhere
    # handles case where vertex 0 = []
    for i in range(len(edges)):
        # can be optimised by storing each vertex's result in a hash table
        if dfs0(edges, set(), i):
            return True

    return False


# we use the visited set to keep track of the vertices currently in the recursive stack
def dfs0(edges, visited, vertex):
    if vertex in visited:
        return True

    # backtracking
    visited.add(vertex)
    found_cycle = False
    for nxt in edges[vertex]:
        found_cycle = found_cycle or dfs0(edges, visited, nxt)
    visited.discard(vertex)

    return found_cycle


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# O(v + e) time | O(v) space - where v is the number of vertices and e is the number of edges in the graph
# time -> basic DFS (we have to consider all the vertices & edges)
def cycleInGraph(edges):
    # # start dfs at each vertex -> loop can start anywhere
    # handles case where vertex 0 = []
    cache = {}
    for i in range(len(edges)):
        if dfs(edges, cache, set(), i):
            return True

    return False


# we use the visited set to keep track of the vertices currently in the recursive stack
def dfs(edges, cache, visited, vertex):
    if vertex in cache:
        return cache[vertex]
    if vertex in visited:  # repeated (found cycle)
        return True

    # backtracking
    visited.add(vertex)
    found_cycle = False
    for nxt in edges[vertex]:
        found_cycle = found_cycle or dfs(edges, cache, visited, nxt)
    visited.discard(vertex)

    cache[vertex] = found_cycle
    return cache[vertex]


"""
edges = [
  [1, 3],
  [2, 3, 4],
  [0],
  [],
  [2, 5],
  [],
]

if starting at 0

visited = {}
vertex = 0

visited = {0}
vertex = 1

visited = {0,1}
vertex = 2

visited = {0,1,2}
vertex = 0

"""
