"""
Construct Binary Search Tree from Preorder Traversal:

Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val,
 and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first,
 then traverses node.left, then traverses node.right.)
It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

After this:
- https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
"""
Reconstruct BST:

The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root node and visits nodes in the following order:
    Current node
    Left subtree
    Right subtree
Given a non-empty array of integers representing the pre-order traversal of a Binary Search Tree (BST),
    write a function that creates the relevant BST and returns its root node.
The input array will contain the values of BST nodes in the order in which these nodes would be visited with a pre-order traversal.
Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property: 
    its value is strictly greater than the values of every node to its left;
    its value is less than or equal to the values of every node to its right;
    and its children nodes are either valid BST nodes themselves or None / null.
Sample Input
    preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
Sample Output
            10 
        /    \
        4      17
    /   \      \
    2     5     19
    /           /
    1           18 
https://www.algoexpert.io/questions/Reconstruct%20BST
"""




from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
use pointers to keep track of valid values for each subtree
"""


class SolutionBF:
    def bstFromPreorderHelper(self, preorder, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(preorder[start])

        node = TreeNode(preorder[start])

        left_start = start + 1
        left_end = left_start
        while left_end <= end and preorder[left_end] < preorder[start]:
            left_end += 1
        left_end -= 1  # last valid value

        node.left = self.bstFromPreorderHelper(preorder, left_start, left_end)
        node.right = self.bstFromPreorderHelper(preorder, left_end+1, end)

        return node

    def bstFromPreorder(self, preorder):
        return self.bstFromPreorderHelper(preorder, 0, len(preorder)-1)


# ----------------------------------------------------------------------------------------------------------------------

"""
We will start by creating the root node while keeping track of the max and min values at any time:
- if value is less than node & greater than min: pass ot to left
- if value is greater than node & less than max: pass to right

Then proceed to the left: passing the max to be the root's value & min to be -inf
                   right: passing the min to be thr root's value & max to be inf
				   

"""


"""
Sample Input
	preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 16, 19, 18]
Sample Output
        10 
      /    \
     4      17 
   /   \   /  \
  2     5 16  19
 /           /
1           18 


keep track of the largest and smallest node that can be placed
left -> pass current node as largest
right -> pass curr node as smallest

if it does not satisfy the constraints we go back up the tree till where it will match
else, insert it

"""


class Solution:
    def bstFromPreorder(self, preorder: List[int]):
        # if not preorder
        return self.bstFromPreorderHelper(preorder, [0], float('-inf'), float('inf'))

    def bstFromPreorderHelper(self, preorder, curr, minimum, maximum):
        if curr[0] >= len(preorder):  # validate curr position on preoder array
            return None

        value = preorder[curr[0]]  # get value from preoder array
        if value < minimum or value > maximum:  # check whether it can be added
            return None

        node = TreeNode(value)  # create Node

        # add left and right
        curr[0] = curr[0] + 1  # move pointer forward
        node.left = self.bstFromPreorderHelper(preorder, curr, minimum, value)
        node.right = self.bstFromPreorderHelper(preorder, curr, value, maximum)

        return node
