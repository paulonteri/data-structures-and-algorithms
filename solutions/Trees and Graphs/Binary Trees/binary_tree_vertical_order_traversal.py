""" 
314. Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Follow up: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""" 
Better solution:
- use BFS
- instead of sorting keep track of the range of the column index (i.e. [min_column, max_column]) and iterate through it
"""


class Solution:
    def verticalOrder(self, root: TreeNode):
        if not root:
            return root

        node_positions = {}
        self.getNodesPositions(root, node_positions)
        # print(node_positions)

        # sort by x
        node_positions_vals = sorted(node_positions, key=lambda x: x)
        for idx, key in enumerate(node_positions_vals):
            node_positions_vals[idx] = node_positions[key]
        # print(node_positions_vals)

        # sort by y
        for items_list in node_positions_vals:
            # print(items_list)
            items_list.sort(key=lambda x: x[0])
            # print(items_list)
            for idx in range(len(items_list)):
                items_list[idx] = items_list[idx][1]  # remove y
        # print(node_positions_vals)
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
