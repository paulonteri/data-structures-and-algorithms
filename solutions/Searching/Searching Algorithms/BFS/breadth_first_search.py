""" 
Breadth-first Search:

You're given a Node class that has a name and an array of optional children nodes.
When put together, nodes form an acyclic tree-like structure.
Implement the breadthFirstSearch method on the Node class, 
which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right),
stores all of the nodes' names in the input array, and returns it.


Sample Input
    graph = A
        /  |  \
        B   C   D
    / \     / \
    E   F   G   H
        / \   \
        I   J   K
Sample Output
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

https://www.algoexpert.io/questions/Breadth-first%20Search
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            curr = queue.pop(0)
            array.append(curr.name)
            for child in curr.children:
                queue.append(child)
        return array


"""
Breadth-first Search:

You're given a Node class that has a name and an array of optional children nodes. 
When put together, nodes form an acyclic tree-like structure.
Implement the breadthFirstSearch method on the Node class, which takes in an empty array,
 traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right),
 stores all of the nodes' names in the input array, and returns it.
 https://www.algoexpert.io/questions/Breadth-first%20Search
"""


# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node0:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node0(name))
        return self

    def breadthFirstSearch(self, array):
        output = []
        queue = [self]  # my implementation of a queue
        while len(queue) > 0:
            curr = queue.pop(0)

            # add current element's name to output_array
            output.append(curr.name)

            queue = queue + curr.children  # add current element's children to end of queue

        return output


"""
[  B   C   D    E   F   G   H]
Sample Input:
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
Sample Output
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]


# Input: graph -> Node class that has a name and an array of optional children nodes
# Output: array of node's names
# Assumptions:
    - the tree will have at least one node
    - all nodes of the tree are valid

# Need to figure out:
    - how to traverse in a BFS method from left to right

# # First Approach: O(n) time | 0(n) space
- have an output_array
- have a queue used to keep track of elements to be traversed next
# add current element's name to output_array
# add current element's children to end of queue
# repeat the above process starting with the first node in the queue
- if the queue is empty, return the output_array
# O(n) time | 0(n) space - where n is the number of nodes in the graph 



"""
