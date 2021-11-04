"""
Subtree of Another Tree:

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

https://leetcode.com/problems/subtree-of-another-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode):
        return self.traverse(s, t)

    def traverse(self, s, t):
        if self.checkSubTreeFunction(s, t) == True:
            return True
        if s is None:
            return False

        return self.traverse(s.left, t) or self.traverse(s.right, t)

    def checkSubTreeFunction(self, s, t):
        if s == None and t == None:
            return True
        elif s == None or t == None or s.val != t.val:
            return False

        return self.checkSubTreeFunction(s.left, t.left) and self.checkSubTreeFunction(s.right, t.right)
