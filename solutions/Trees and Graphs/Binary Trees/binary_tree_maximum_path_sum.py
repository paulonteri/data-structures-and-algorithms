"""
Max Path Sum In Binary Tree:
Binary Tree Maximum Path Sum:

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.

Write a function that takes in a Binary Tree and returns its max path sum.
A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes;
 a path sum is the sum of the values of the nodes in a particular path.
Each BinaryTree node has an integer value, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
    tree = 1
        /     \
      2       3
    /   \   /   \
    4     5 6     7
Sample Output
    18 // 5 + 2 + 1 + 3 + 7

https://www.algoexpert.io/questions/Max%20Path%20Sum%20In%20Binary%20Tree
https://leetcode.com/problems/binary-tree-maximum-path-sum
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        if not root:
            return 0
        return self.max_path(root)[0]

    def max_path(self, root):
        if not root:
            return float("-inf"), float("-inf")

        left = self.max_path(root.left)
        right = self.max_path(root.right)

        max_as_path = max(root.val,
                          root.val + left[1],
                          root.val + right[1],)

        maximum = max(max_as_path,  # Max as path
                      root.val + left[1] + right[1],  # Max as tree
                      left[0],  # Prev max
                      right[0])  # Prev max

        return maximum, max_as_path


""" 
"""


class TreeInfo:

    def __init__(self, max_as_branch, max_as_branch_or_triangle):
        self.max_as_branch = max_as_branch
        # max continuous path as branch/tree
        self.max_as_branch_or_triangle = max_as_branch_or_triangle


# O(n) time
# O(log(n)) space - because it is a binary tree
def maxPathSum(tree):
    res = maxPathSumHelper(tree)
    return res.max_as_branch_or_triangle


def maxPathSumHelper(tree):
    if not tree:
        # handle negatives with float('-inf')
        # return TreeInfo(float('-inf'), float('-inf')) # <- also works.
        return TreeInfo(0, float('-inf'))

    left = maxPathSumHelper(tree.left)
    right = maxPathSumHelper(tree.right)

    # longest continuous branch/straight line.
    curr_max_as_branch = max(
        tree.value,
        tree.value + left.max_as_branch,
        tree.value + right.max_as_branch
    )

    # longest branch/triangle we have seen so far note: curr_max_as_branch is automatically included
    curr_max_as_branch_or_triangle = max(
        curr_max_as_branch,
        tree.value + left.max_as_branch + right.max_as_branch,  # curr_max_as_triangle
        left.max_as_branch_or_triangle,
        right.max_as_branch_or_triangle
    )

    return TreeInfo(curr_max_as_branch, curr_max_as_branch_or_triangle)
