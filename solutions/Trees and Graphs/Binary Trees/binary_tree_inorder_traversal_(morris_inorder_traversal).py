""" 
Morris Inorder Tree Traversal - Inorder with O(1) space

https://leetcode.com/problems/binary-tree-inorder-traversal
EPI 9.11
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        res = []

        curr = root
        while curr is not None:

            # has no left child - so is the next valid
            if not curr.left:
                res.append(curr.val)
                curr = curr.right

            # place the curr node as the right child of its predecessor
            #   which is the rightmost node in the left subtree
            else:
                predecessor = self.get_inorder_predecessor(curr)

                # # move node down the tree
                left = curr.left
                curr.left = None  # prevent loop

                predecessor.right = curr

                # # continue to left subtree
                curr = left

        return res

    def get_inorder_predecessor(self, node):
        curr = node.left

        while curr.right is not None:
            curr = curr.right

        return curr
