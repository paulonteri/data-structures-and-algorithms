"""
Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

https://leetcode.com/problems/binary-tree-paths
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root):
        paths = []
        if not root:
            return paths

        stack = [(root, [str(root.val)])]
        while stack:
            node, path = stack.pop()

            # leaf node
            if not node.left and not node.right:
                paths.append("->".join(path))
                continue

            if node.left:
                stack.append((node.left, path+[str(node.left.val)]))
            if node.right:
                stack.append((node.right, path+[str(node.right.val)]))

        return paths
