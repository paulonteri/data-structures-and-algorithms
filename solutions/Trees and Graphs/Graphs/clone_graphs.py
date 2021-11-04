"""
Clone Graph:

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
    class Node {
        public int val;
        public List<Node> neighbors;
    }

Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. 

The graph is represented in the test case using an adjacency list.
Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

https://leetcode.com/problems/clone-graph/
"""

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node'):
        if node is None:
            return None

        created_nodes = []  # node 1 will be at index 0,  2 at 1...

        return self.createNode(node, created_nodes)

    def createNode(self, node: Node, created_nodes):
        # ensure we have the index: node 1 will be at index 0,  2 at 1...
        while len(created_nodes) < node.val:
            created_nodes.append(None)
        # check if created: no need to create it again
        if created_nodes[node.val-1] is not None:
            return created_nodes[node.val-1]

        # # create new node
        new_node = Node(node.val)
        # add to created_nodes
        created_nodes[node.val-1] = new_node

        # create neighbors
        if node.neighbors:
            neighbors = []
            for neighbour in node.neighbors:
                neighbors.append(self.createNode(neighbour, created_nodes))
            new_node.neighbors = neighbors

        return new_node


"""
1. create new node
2. add children to node
    - create child
    
node
node.neighnours = [createNode(child1), createNode(child2)
"""
