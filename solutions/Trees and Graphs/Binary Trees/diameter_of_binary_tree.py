"""
Binary Tree Diameter:
Diameter of Binary Tree:

Write a function that takes in a Binary Tree and returns its diameter. 
The diameter of a binary tree is defined as the length of its longest path, even if that path doesn't pass through the root of the tree.
A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes. 
The length of a path is the number of edges between the path's first node and its last node.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

https://www.algoexpert.io/questions/Binary%20Tree%20Diameter
https://leetcode.com/problems/diameter-of-binary-tree/
"""


"""
Sample Input
tree =        1
            /  \
           3     2
             \ 
        7     4
       /       \
      8         5
     /           \
    9             6
Sample Output
	6 // 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6
	// There are 6 edges between the
	// first node and the last node
	// of this tree's longest path.
	
Sample Input
tree =  1

Sample Output
	0
"""

""" 
The key observation to make is: 
    the longest path has to be between two leaf nodes. 
We can prove this with contradiction. 
Imagine that we have found the longest path, and it is not between two leaf nodes. 
We can extend that path by 1, by adding the child node of one of the end nodes (as at least one must have a child, given that they aren't both leaves). 
This contradicts the fact that our path is the longest path. Therefore, the longest path must be between two leaf nodes.

Moreover, we know that in a tree, nodes are only connected with their parent node and 2 children. 
Therefore we know that the longest path in the tree would consist of a node, its longest left branch, and its longest right branch. 
So, our algorithm to solve this problem will find the node where the sum of its longest left and right branches is maximized. 
This would hint at us to apply Depth-first search (DFS) to count each node's branch lengths, 
 because it would allow us to dive deep into the leaves first, and then start counting the edges upwards.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        diameter = 0

        def diameter_helper(root):
            if not root:
                return 0
            nonlocal diameter

            left = diameter_helper(root.left)
            right = diameter_helper(root.right)

            diameter = max(left + right,  # Connect left & right branches
                           diameter)

            # Create a branch that will be used to calculate longest_path by the root's parent node

            # we do not add the curr node's height/depth to any of the calculations/results for the longest_diameter,
            # 	it is only considered from its parent node
            #   because if tree = 1 (node), longest_diameter = 0
            return max(left, right) + 1

        diameter_helper(root)
        return diameter


""""""

# This is an input class. Do not edit.


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# ---------------------------------------------------------------------------------------------------------------------


def binaryTreeDiameter3(tree):
    max_diameter = [-1]
    depths(tree, max_diameter)
    return max_diameter[0]


def depths(node, max_diameter):
    if node is None:
        return 0

    # calculate diameter
    left = depths(node.left, max_diameter)
    right = depths(node.right, max_diameter)
    max_diameter[0] = max(max_diameter[0], left+right)

    return max(left, right) + 1  # add node to depth


# ---------------------------------------------------------------------------------------------------------------------


def binaryTreeDiameter(tree):
    return binaryTreeDiameterHelper(tree, 0).longest_diameter


class Result:
    def __init__(self, longest_path, longest_diameter):
        self.longest_path = longest_path
        self.longest_diameter = longest_diameter

    def __str__(self):  # for debugging
        return f"{self.longest_path} {self.longest_diameter}"


def binaryTreeDiameterHelper(tree, depth):
    if tree is None:
        return Result(0, 0)

    left = binaryTreeDiameterHelper(tree.left, depth+1)
    right = binaryTreeDiameterHelper(tree.right, depth+1)

    curr_diameter = left.longest_path + right.longest_path
    prev_longest_diameter = max(left.longest_diameter, right.longest_diameter)

    curr_longest_diameter = max(
        curr_diameter,
        prev_longest_diameter,
    )

    # we do not add the curr node's height/depth to any of the calculations/results for the longest_diameter,
    # 	it is only considered from its parent node
    #   because if tree = 1 (node), longest_diameter = 0
    nxt_longest_path = max(left.longest_path, right.longest_path) + 1
    return Result(nxt_longest_path, curr_longest_diameter)
