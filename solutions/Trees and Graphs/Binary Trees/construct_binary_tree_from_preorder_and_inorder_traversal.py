"""
Construct Binary Tree from Preorder and Inorder Traversal:

Given two integer arrays preorder and inorder where
preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Example 1:
    Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    Output: [3,9,20,null,null,15,7]
Example 2:
    Input: preorder = [-1], inorder = [-1]
    Output: [-1]

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------------------------------------------------------------------------------------------------------------------


""" 
- The root will be the first element in the preorder sequence
- Next, locate the index of the root node in the inorder sequence
    - this will help you know the number of nodes to its left & the number to its right
- repeat this recursively
"""


class SolutionBF(object):
    def buildTree(self, preorder, inorder):
        return self.dfs(preorder, inorder)

    def dfs(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.dfs(preorder[1: mid+1], inorder[: mid])
        root.right = self.dfs(preorder[mid+1:], inorder[mid+1:])
        return root


class SolutionBF0:
    def buildTree(self, preorder, inorder):

        if len(inorder) == 0:
            # the remaining preorder values do not belong in this subtree
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        ino_index = inorder.index(preorder.pop(0))  # remove from preorder
        node = TreeNode(inorder[ino_index])

        node.left = self.buildTree(preorder, inorder[:ino_index])
        node.right = self.buildTree(preorder, inorder[ino_index+1:])

        return node


class SolutionBF00:
    def buildTree(self, preorder, inorder):

        preorder_pos = 0

        def buildTreeHelper(preorder, inorder):
            nonlocal preorder_pos

            # we do not have valid nodes to be placed
            if len(inorder) == 0:  # invalid side
                return
            if preorder_pos >= len(preorder):
                return

            # # create node
            # node
            inorder_idx = inorder.index(preorder[preorder_pos])
            preorder_pos += 1
            node = TreeNode(inorder[inorder_idx])

            # children -> will pass only valid children below -> (inorder[:inorder_idx] & inorder[inorder_idx+1:] does that)
            node.left = buildTreeHelper(preorder, inorder[:inorder_idx])
            node.right = buildTreeHelper(preorder, inorder[inorder_idx+1:])

            return node
        return buildTreeHelper(preorder, inorder)
#         def buildTreeHelper2( preorder, inorder):
#             nonlocal preorder_pos

#             if preorder_pos >= len(preorder):
#                 return

#             # # create node
#             # node
#             inorder_idx = inorder.index( preorder[preorder_pos] )
#             preorder_pos += 1
#             node = TreeNode(inorder[inorder_idx ])


#             left = inorder[:inorder_idx]
#             right = inorder[inorder_idx+1:]
#             if left:
#                 node.left = buildTreeHelper(preorder, left)
#             if right:
#                 node.right = buildTreeHelper(preorder, right)

#             return node
#       return buildTreeHelper2(preorder, inorder)

# ---------------------------------------------------------------------------------------------------------------------


""" 
- The root will be the first element in the preorder sequence
- Next, locate the index of the root node in the inorder sequence
    - this will help you know the number of nodes to its left & the number to its right
- repeat this recursively

- iterate through the preorder array and check if the current can be placed in the current tree(or recursive call)

- We use the remaining inorder traversal to determine(restrict) whether
    the current preorder node is in the left or right
"""


class Solution:
    def buildTree(self, preorder, inorder):
        preorder_pos = 0
        inorder_idxs = {val: idx for idx, val in enumerate(inorder)}

        def helper(inorder_left, inorder_right):
            nonlocal preorder_pos

            if preorder_pos == len(preorder):
                return
            if inorder_left > inorder_right:
                return

            val = preorder[preorder_pos]
            preorder_pos += 1

            node = TreeNode(val)

            inorder_idx = inorder_idxs[val]
            # start with left !
            node.left = helper(inorder_left, inorder_idx-1)
            node.right = helper(inorder_idx+1, inorder_right)

            return node

        return helper(0, len(inorder)-1)
