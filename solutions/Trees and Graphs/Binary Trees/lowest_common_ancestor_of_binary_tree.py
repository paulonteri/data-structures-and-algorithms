"""
Lowest Common Ancestor of a Binary Tree:

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has 
    both p and q as descendants (where we allow a node to be a descendant of itself).”
    
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return self.lowestCommonAncestorHelper(root, p, q)

    def lowestCommonAncestorHelper(self,  curr, p, q):
        if curr is None:
            return None

        left = self.lowestCommonAncestorHelper(curr.left, p, q)
        right = self.lowestCommonAncestorHelper(curr.right, p, q)

        # found common ancestor
        if left == True and right == True:
            return curr
        elif (curr.val == p.val or curr.val == q.val) and (left == True or right == True):
            return curr

        # found p/q in current subtree
        elif curr.val == p.val or curr.val == q.val or left == True or right == True:
            return True

        # return the common ancestor
        return left or right
