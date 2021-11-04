""" 
Validate Three Nodes:

You're given three nodes that are contained in the same Binary Search Tree: nodeOne, nodeTwo, and nodeThree. 
Write a function that returns a boolean representing whether one of nodeOne or nodeThree is an ancestor of nodeTwo and the other node is a descendant of nodeTwo. 
For example, if your function determines that nodeOne is an ancestor of nodeTwo, then it needs to see if nodeThree is a descendant of nodeTwo. 
If your function determines that nodeThree is an ancestor, then it needs to see if nodeOne is a descendant.
A descendant of a node N is defined as a node contained in the tree rooted at N. 
A node N is an ancestor of another node M if M is a descendant of N.
It isn't guaranteed that nodeOne or nodeThree will be ancestors or descendants of nodeTwo, 
    but it is guaranteed that all three nodes will be unique and will never be None / null. In other words, you'll be given valid input nodes.
Each BST node has an integer value, a left child node, and a right child node. 
A node is said to be a valid BST node if and only if it satisfies the BST property: 
    its value is strictly greater than the values of every node to its left; 
    its value is less than or equal to the values of every node to its right; 
    and its children nodes are either valid BST nodes themselves or None / null.

https://www.algoexpert.io/questions/Validate%20Three%20Nodes
"""

# This is an input class. Do not edit.


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


""" 
------------------------------------------------------------------------------------------------------------------------------------------------

if node1 is the descendant of node2, then node2 must be the descendant of node3 
if node3 is the descendant of node2, then node2 must be the descendant of node1
"""


# O(h) time | O(1) space - where h is the height of the tree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDescendant(nodeTwo, nodeThree):
        return isDescendant(nodeOne, nodeTwo)
    if isDescendant(nodeTwo, nodeOne):
        return isDescendant(nodeThree, nodeTwo)
    return False


def isDescendant(parent, child):
    curr = parent
    while curr is not None:
        if child.value < curr.value:
            curr = curr.left
        elif child.value > curr.value:
            curr = curr.right
        else:
            return True
    return False


""" 
------------------------------------------------------------------------------------------------------------------------------------------------

 - find node one/three
 - find node two
 - find node one/three (the one that wasn't found in step one)
 
 - if we find any of them in a different order, return False
"""
