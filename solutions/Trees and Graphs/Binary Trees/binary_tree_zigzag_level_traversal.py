"""
Binary Tree Zigzag Level Order Traversal:

Given a binary tree, return the zigzag level order traversal of its nodes' values.
 (ie, from left to right, then right to left for the next level and alternate between).

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        res = []
        self.zigzagHelper(root, res, 1)
        return res

    def zigzagHelper(self, root, res, level):
        if not root:
            return

        if len(res) < level:
            # add array for level
            res.append([])

        if level % 2 == 0:  # right to left
            res[level-1].insert(0, root.val)
        else:  # left to right
            res[level-1].append(root.val)

        self.zigzagHelper(root.left, res, level+1)
        self.zigzagHelper(root.right, res, level+1)
