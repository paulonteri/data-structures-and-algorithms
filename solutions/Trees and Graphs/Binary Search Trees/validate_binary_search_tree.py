"""
Validate Binary Search Tree:

Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
    / \
    1   3

    Input: [2,1,3]
    Output: true

Example 2:

    5
    / \
    1   4
        / \
        3   6

    Input: [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
    
https://leetcode.com/problems/validate-binary-search-tree/
https://www.algoexpert.io/questions/Validate%20BST
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    # O(n) time | O(n) space - because of the recursion call stack
    def isValidBST(self, root):
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, tree, minimum, maximum):

        # past leaf node/ single node tree
        if tree == None:
            return True

        # validate
        if tree.val >= maximum or tree.val <= minimum:
            return False

        # every node to the left is smaller than the one above it. the one above it is larger.
        left_handler = self.validate(
            tree.left, minimum=minimum, maximum=tree.val)

        # every node to the right is larger. the one above it is smaller.
        right_handler = self.validate(
            tree.right, minimum=tree.val, maximum=maximum)

        return left_handler and right_handler
        # return self.validate(tree.left, minimum=minimum, maximum=tree.val) and self.validate(tree.right, minimum=tree.val, maximum=maximum)


#  O(n) time | O(d) space | where d is the depth of the tree (because of the callstack)
def validateBst(node, maximum=float('inf'), minimum=float('-inf')):
    if node is None:
        return True  # we didn't find an invalid node

    if node.value >= maximum or node.value < minimum:  # validate with max & min
        return False

    # for every left child, it's maximum will be the value of it's parent and
    # for every right child, it's minimum will be the value of it's parent
    return validateBst(node.left, maximum=node.value, minimum=minimum) \
        and validateBst(node.right, maximum=maximum, minimum=node.value)
