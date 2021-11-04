"""
Invert Binary Tree:

Write a function that takes in a Binary Tree and inverts it. 
In other words, the function should swap every left node in the tree for its corresponding right node.
Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.

https://www.algoexpert.io/questions/Invert%20Binary%20Tree
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    if tree is None:
        return

    # swap
    prev_left = tree.left
    tree.left = tree.right
    tree.right = prev_left

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
