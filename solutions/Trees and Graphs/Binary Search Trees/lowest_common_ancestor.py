"""
Lowest Common Ancestor of a Binary Search Tree:

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
 (where we allow a node to be a descendant of itself).”

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr = root

        while True:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right

            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left

            else:
                break

        return curr


"""
First Approach:
- take advantage of BST's properties: skip all valid ancestors
"""
