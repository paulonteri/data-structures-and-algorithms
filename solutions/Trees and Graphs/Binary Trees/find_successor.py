"""
Find Successor:

Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node)
 as well as a node contained in that tree and returns the given node's successor.
A node's successor is the next node to be visited (immediately after the given node) 
 when traversing its tree using the in-order tree-traversal technique.
A node has no successor if it's the last node to be visited in the in-order traversal.
If a node has no successor, your function should return None / null.
Each BinaryTree node has an integer value, a parent node, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
    tree = 
                1
             /   \
            2     3
          /   \ 
         4     5
        /       
        6  
    node = 5   
Sample Output
    1
    // This tree's in-order traversal order is:
    // 6 -> 4 -> 2 -> 5 -> 1 -> 3 
    // 1 comes immediately after 5.

https://www.algoexpert.io/questions/Find%20Successor
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if tree is None:
        return

    left = findSuccessor(tree.left, node)
    if tree == node:
        return findSuccessorHelper(tree, node)
    right = findSuccessor(tree.right, node)

    return left or right


def findSuccessorHelper(tree, node):

    # if has a right child
    # will be left most node of right child
    if tree.right is not None:
        # find left most in right subtree
        left_most = tree.right
        while left_most.left is not None:
            left_most = left_most.left
        return left_most

    # no right child -> successor is ancestor:
    # find ancestor where child is left child
    else:

        # find where we first branched left
        while tree is not None:
            if tree.parent is not None and tree == tree.parent.left:
                return tree.parent

            tree = tree.parent

    return None


"""
If a node has a right subtree:
- its successor is the futhest left node in the right subtree
else: 
- its successor is the first point where we turned left
-    i.e if tree == tree.parent.left, return tree.parent

Sample Input
tree = 
              1
            /   \
           2     3
         /   \ 
        4     5
       /     /  \
      6  	7	8

node = 5   
output = 8

node = 8   
output = 1

node = 2   
output = 7

node = 1   
output = 3


"""
