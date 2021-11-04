""" 
Inorder Successor in BST:
FIND THE FIRST KEY GREATER THAN A GIVEN VALUE IN A BST:

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. 
If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

https://leetcode.com/problems/inorder-successor-in-bst
epi 14.2

https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#fa170f4d75aa4e01b8d0c403220a83e2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode'):
        nxt = None

        curr = root
        while curr is not None:
            # successor will be the next larger value compared to the element
            if curr.val > p.val:
                nxt = curr
                # try to reduce the value
                curr = curr.left
            else:
                # try to increase the value
                curr = curr.right

        return nxt
