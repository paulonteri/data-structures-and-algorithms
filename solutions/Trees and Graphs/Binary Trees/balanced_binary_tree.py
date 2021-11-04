"""
Height Balanced Binary Tree:

You're given the root node of a Binary Tree. 
Write a function that returns true if this Binary Tree is height balanced and false if it isn't.
A Binary Tree is height balanced if for each node in the tree, 
 the difference between the height of its left subtree and the height of its right subtree is at most 1.
Each BinaryTree node has an integer value, a left child node, and a right child node.
Children nodes can either be BinaryTree nodes themselves or None / null.

Sample Input
    tree = 1
        /   \
        2     3
    /   \     \
    4     5     6
        /   \
        7     8
Sample Output
    true

https://leetcode.com/problems/balanced-binary-tree
https://www.algoexpert.io/questions/Height%20Balanced%20Binary%20Tree
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    return heightBalancedBinaryTreeHelper(tree)[0]


def heightBalancedBinaryTreeHelper(tree):
    if tree is None:
        return True, 0

    left = heightBalancedBinaryTreeHelper(tree.left)
    right = heightBalancedBinaryTreeHelper(tree.right)

    height_diff = abs(left[1] - right[1])
    is_balanced = left[0] and right[0] and height_diff <= 1

    curr_height = 1 + max(left[1], right[1])

    return is_balanced, curr_height


"""
Sample Input
	tree = 1
		 /   \
		2     3
	  /   \     \
	 4     5     6
		 /   \
		7     8
Sample Output
	true
	
Sample Input
	tree = 1
		 /   \
		2     3
	  /   \     \
	 4     5     6
		 /   \    \ 
		7     8    9
Sample Output
	false (coz of 3)
	
	
"""
