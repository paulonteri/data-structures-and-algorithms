""" 
Find Nodes Distance K:

You're given the root node of a Binary Tree, a target value of a node that's contained in the tree, and a positive integer k. 
Write a function that returns the values of all the nodes that are exactly distance k from the node with target value.
The distance between two nodes is defined as the number of edges that must be traversed to go from one node to the other. 
For example, the distance between a node and its immediate left or right child is 1. The same holds in reverse: the distance between a node and its parent is 1. In a tree of three nodes where the root node has a left and right child, the left and right children are distance 2 from each other.

Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

Note that all BinaryTree node values will be unique, and your function can return the output values in any order.

Sample Input
tree = 1
     /   \
    2     3
  /   \     \
 4     5     6
           /   \
          7     8
target = 3
k = 2
Sample Output
[2, 7, 8] // These values could be ordered differently.

https://www.algoexpert.io/questions/Find%20Nodes%20Distance%20K
"""
""" 
All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, 
    return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.
Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
    Output: [7,4,1]
    Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
- a graph representation of this will make it easier

- find/record parents
- dfs from target
"""


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        res = []
        parents = {}
        self.recordParents(root, parents, None)
        self.findNodesDistanceK(target, parents, k, res, target)
        return res

    def findNodesDistanceK(self, root, parents, k, res, prev):
        if root is None:
            return

        if k == 0:
            res.append(root.val)
            return

        if root.left != prev:  # left
            self.findNodesDistanceK(root.left, parents, k-1, res, root)
        if root.right != prev:  # right
            self.findNodesDistanceK(root.right, parents, k-1, res, root)
        if parents[root.val] != prev:  # parent
            self.findNodesDistanceK(parents[root.val], parents, k-1, res, root)

    def recordParents(self, root, parents, parent):
        if root is None:
            return

        parents[root.val] = parent
        self.recordParents(root.left, parents, root)
        self.recordParents(root.right, parents, root)
