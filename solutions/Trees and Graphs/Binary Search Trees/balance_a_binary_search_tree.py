""" 
1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. 
If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

https://leetcode.com/problems/balance-a-binary-search-tree

similar to Min Height BST
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" 
1. convert tree to sorted array using inorder traversal
2. build the tree from the sorted array
    - the root will be the middle of the array
    - the left of the middle will be passed to a recursive function to build the left children
    - the right of the middle will be passed to a recursive function to build the right children

"""


class Solution:
    def balanceBST(self, root: TreeNode):
        array = []
        self.inOrderTraverse(root, array)
        return self.buildTree(array, 0, len(array)-1)

    def buildTree(self, array, start, end):
        if start > end:
            return None

        mid = (start+end) // 2

        curr = array[mid]
        curr.left = self.buildTree(array, start, mid-1)
        curr.right = self.buildTree(array, mid+1, end)

        return curr

    def inOrderTraverse(self, root, array):
        stack = []
        curr = root
        while curr or stack:
            # if has a left child, move left
            while curr and curr.left:
                stack.append(curr)
                curr = curr.left

            # curr is either the left most value or None
            # if none take the left-most from the top of stack
            if curr is None:
                curr = stack.pop()

            array.append(curr)
            # we are at the left most value so the only possible next place to go is right
            curr = curr.right
