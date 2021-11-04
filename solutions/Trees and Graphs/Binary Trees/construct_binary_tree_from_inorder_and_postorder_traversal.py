""" 
106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where 
    inorder is the inorder traversal of a binary tree and 
    postorder is the postorder traversal of the same tree, 
construct and return the binary tree.


Example 1:
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]
Example 2:
    Input: inorder = [-1], postorder = [-1]
    Output: [-1]

https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        postorder_idx = len(postorder)-1
        inorder_idxs = {val: idx for idx, val in enumerate(inorder)}

        def helper(inorder_left, inorder_right):
            nonlocal postorder_idx

            if postorder_idx < 0:
                return None
            if inorder_left > inorder_right:
                return None

            val = postorder[postorder_idx]
            postorder_idx -= 1

            # create node
            node = TreeNode(val)

            inorder_idx = inorder_idxs[val]
            # start with right !
            node.right = helper(inorder_idx+1, inorder_right)
            node.left = helper(inorder_left, inorder_idx-1)

            return node
        return helper(0, len(inorder)-1)
