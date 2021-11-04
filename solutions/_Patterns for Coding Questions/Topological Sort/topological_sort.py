""" 
Topological Sort:

Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices
 such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:
    Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
    Output: Following are the two valid topological sorts for the given graph:
    1) 3, 2, 0, 1
    2) 3, 2, 1, 0

Example 2:
    Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
    Output: Following are all valid topological sorts for the given graph:
    1) 4, 2, 3, 0, 1
    2) 4, 3, 2, 0, 1
    3) 4, 3, 2, 1, 0
    4) 4, 2, 3, 1, 0
    5) 4, 2, 0, 3, 1

Example 3:
    Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
    Output: Following are all valid topological sorts for the given graph:
    1) 5, 6, 3, 4, 0, 1, 2
    2) 6, 5, 3, 4, 0, 1, 2
    3) 5, 6, 4, 3, 0, 2, 1
    4) 6, 5, 4, 3, 0, 1, 2
    5) 5, 6, 3, 4, 0, 2, 1
    6) 5, 6, 3, 4, 1, 2, 0

    There are other valid topological ordering of the graph too.

Source: Any node that has no incoming edge and has only outgoing edges is called a source.
Sink: Any node that has only incoming edges and no outgoing edge is called a sink.

https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00
"""
import collections

""" 
Solution:

To find the topological sort of a graph we can traverse the graph in a Breadth-First Search (BFS) way. 
We will start with all the sources, and in a stepwise fashion, save all sources to a sorted list. 
We will then remove all sources and their edges from the graph. After the removal of the edges, 
    we will have new sources, so we will repeat the above process until all vertices are visited.
This is how we can implement this algorithm:

1. Initialization
    - We will store the graph in Adjacency Lists, which means each parent vertex will have a list containing all of its children. 
        We will do this using a HashMap where the ‘key’ will be the parent vertex number and the value will be a List containing children vertices.
    - To find the sources, we will keep a HashMap to count the in-degrees 
        i.e., count of incoming edges of each vertex. Any vertex with ‘0’ in-degree will be a source.
2. Build the graph and find in-degrees of all vertices
    - We will build the graph from the input and populate the in-degrees HashMap.
3. Find all sources
    - All vertices with ‘0’ in-degrees will be our sources and we will store them in a Queue.
4. Sort
    - For each source, do the following things:
        - Add it to the sorted list.
        - Get all of its children from the graph.
        - Decrement the in-degree of each child by 1.
        - If a child’s in-degree becomes ‘0’, add it to the sources Queue.
    - Repeat the step above, until the source Queue is empty.
"""


# import collections

def topological_sort_0(vertices, edge_list):
    sorted_order = []

    # # convert edge list to an adjacency list & record the edge depths
    # graph
    adjacency_list = collections.defaultdict(list)
    # count of incoming edges of each vertex/node or how many parents it has (used to determine sources)
    in_degree = collections.defaultdict(int)
    for edge in edge_list:
        parent, child = edge[0], edge[1]
        adjacency_list[parent].append(child)
        in_degree[child] += 1  # increment child's in_degree

    # # find all sources (have no parents)
    queue = []
    for key in adjacency_list:
        if in_degree[key] == 0:
            queue.append(key)

    # # add into sorted_order each source
    while len(queue) > 0:
        vertex = queue.pop(0)
        sorted_order.append(vertex)
        # decrement the in-degree of each child by 1 & if a child’s in-degree becomes ‘0’, add it to the sources Queue.
        for child in adjacency_list[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return sorted_order

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


""" 
Solution:

An easy way to find a topological ordering with trees is to iteratively pick off the leaf nodes. 
It's like you're cherry-picking from the bottom, it doesn't matter the order you do it. This procedure continues until no more nodes are left...
    1. First find an unvisited node, it doesn't matter which.
    2. From this node do a Depth First Search exploring only reachable unvisited nodes.
    3. On recursive callbacks add the current node to the topological ordering in reverse order.

https://www.youtube.com/watch?v=eL-KzMXSXXI
"""

# import collections


def dfs(graph, visited, vertex, sorted_order):
    if visited[vertex]:
        return

    for child in graph[vertex]:
        dfs(graph, visited, child, sorted_order)

    visited[vertex] = True
    sorted_order.append(vertex)


def topological_sort(vertices, edge_list):
    sorted_order = []

    # # convert edge list to an adjacency list & record the edge depths
    adjacency_list = collections.defaultdict(list)
    for edge in edge_list:
        adjacency_list[edge[0]].append(edge[1])

    visited = collections.defaultdict(bool)

    for edge in edge_list:
        dfs(adjacency_list, visited, edge[0], sorted_order)

    sorted_order.reverse()
    return sorted_order


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
