"""
Maximum Depth of Binary Tree:

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the
 longest path from the root node down to the farthest leaf node.

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode):
        return self.maxDepthHelper(root)

    def maxDepthHelper(self, root):
        if not root:
            return 0

        left = self.maxDepthHelper(root.left)
        right = self.maxDepthHelper(root.right)

        return max(left, right) + 1


class Solution2:
    def maxDepth(self, root: TreeNode):
        if not root:
            return 0

        # stack = [(node, depth)]
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, cur_depth = stack.pop()
            if node:
                max_depth = max(max_depth, cur_depth)
                #
                if node.left:
                    stack.append((node.left, cur_depth+1))
                if node.right:
                    stack.append((node.right, cur_depth+1))

        return max_depth
