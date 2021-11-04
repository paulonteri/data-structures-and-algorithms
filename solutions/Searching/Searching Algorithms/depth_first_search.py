"""
Depth-first Search:

You're given a Node class that has a name and an array of optional children nodes.
When put together, nodes form an acyclic tree-like structure.
Implement the depthFirstSearch method on the Node class, which takes in an empty array,
 traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right),
 stores all of the nodes' names in the input array, and returns it.
https://www.algoexpert.io/questions/Depth-first%20Search
"""


class Node00:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        self._depthFirstSearchHelper(array, self)
        return array

    def _depthFirstSearchHelper(self, array, node):
        array.append(node.name)

        for child in node.children:
            self._depthFirstSearchHelper(array, child)

    def depthFirstSearch2(self, array):
        stack = [self]  # mock stack
        while stack:

            curr = stack.pop(0)
            array.append(curr.name)

            for idx in reversed(range(len(curr.children))):  # add from last to first
                # items in stack are added to the top
                stack.insert(0, curr.children[idx])

        return array


"""
Sample Input
    graph = A
        /  |  \
        B   C   D
    / \     / \
    E   F   G   H
        / \   \
        I   J   K
Sample Output
    ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]



Solution:
1. Add node to input array
2. Recurse through the node's children starting with the first
3. Repeat

1. Add node to input array (the top node in the stack)
2. Add node's children to stack (from last to first)
3. Repeat

"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def depthFirstSearch(self, array):
        self._depthFirstSearchHelper(array)
        return array

    def _depthFirstSearchHelper(self, array):
        array.append(self.name)

        for child in self.children:
            child._depthFirstSearchHelper(array)


class Tree:
    def __init__(self, name):
        self.children = []
        self.name = name

    def depthFirstSearch(self, array):
        stack = [self]

        while len(stack) > 0:
            curr = stack.pop()
            array.append(curr.name)
            for idx in reversed(range(len(curr.children))):
                stack.append(curr.children[idx])

        return array
