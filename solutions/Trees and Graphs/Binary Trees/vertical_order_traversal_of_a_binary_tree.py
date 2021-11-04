"""
Vertical Order Traversal of a Binary Tree:

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.
The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right. 
Each report is a list of all nodes at a given x-coordinate. The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest. 
If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.
Return the vertical order traversal of the binary tree.

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Prerequisite: https://leetcode.com/problems/binary-tree-vertical-order-traversal/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode):
        if not root:
            return root

        node_positions = {}
        self.getNodesPositions(root, node_positions)

        # sort by x
        node_positions_vals = sorted(node_positions, key=lambda x: x)
        for idx, key in enumerate(node_positions_vals):
            node_positions_vals[idx] = node_positions[key]

        # sort by y
        for items_list in node_positions_vals:
            items_list.sort(key=lambda x: x[0])
            for idx in range(len(items_list)):
                items_list[idx] = items_list[idx][1]  # remove y

        return node_positions_vals

    # get each node's position
    # x will represent 'columns' and y 'rows'
    def getNodesPositions(self, node, node_positions, x=0, y=0):
        if node is None:
            return None

        if x not in node_positions:
            node_positions[x] = []

        node_positions[x] = node_positions[x]+[[y, node.val]]
        self.getNodesPositions(node.left, node_positions, x-1, y+1)
        self.getNodesPositions(node.right, node_positions, x+1, y+1)


""" 
Solution 2: BFS with queue
- explained in EPI
"""
