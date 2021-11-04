"""
Binary Tree Right Side View:

Given a binary tree, imagine yourself standing on the right side of it,
 return the values of the nodes you can see ordered from top to bottom.

https://leetcode.com/problems/binary-tree-right-side-view
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode):
        output = []
        self.traverse(root, 0, output)
        return output

    def traverse(self, node, level, output):
        if node is None:
            return

        # visit node
        if len(output)-1 < level:
            output.append(node.val)

        self.traverse(node.right, level+1, output)
        self.traverse(node.left, level+1, output)
