"""
Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

https://leetcode.com/problems/path-sum-ii/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# O(n) time | O(n) space
class Solution:
    def pathSum(self, root, sum):
        all_paths = []
        self._path_finder(root, sum, [], all_paths)
        return all_paths

    def _path_finder(self, curr, s, curr_path, allPaths):
        if curr is None:
            return

        # # gives us error solvable by backtracking
        # curr_path.append(curr.val)
        # curr_path  += [curr.val]
        curr_path = curr_path + [curr.val]
        s = s - curr.val

        # if the current node is a leaf and subrating it from s will give you 0, we have found a path, save the current path
        if s == 0 and not curr.left and not curr.right:
            # adds empty list ??? when I use curr_path.append(curr.val)
            allPaths.append(curr_path)
            # allPaths.append(list(curr_path)) # use this instead when using curr_path.append(curr.val)

        else:
            # traverse the left & right sub-tree
            self._path_finder(curr.left,
                              s, curr_path, allPaths)
            self._path_finder(curr.right,
                              s, curr_path, allPaths)

        # # in case we use curr_path.append(curr.val) instead of curr_path = curr_path + [curr.val] above, we will have to backtrack
        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        # del curr_path[-1]


"""
Example:

Given the below binary tree and sum = 22,

        5
        / \
        4   8
    /   / \
    11  13  4
    /  \    / \
    7    2  5   1
Return:

    [
    [5,4,11,2],
    [5,8,4,5]
    ]
"""


# -------------------------------------------------------------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution00:
    def pathSum(self, root, targetSum):
        if not root:
            return []

        targetSum -= root.val
        if targetSum == 0:
            if not root.left and not root.right:  # leaf
                return [[root.val]]

        left = self.pathSum(root.left, targetSum)
        right = self.pathSum(root.right, targetSum)

        res = []
        for arr in right:
            res.append([root.val]+arr)
        for arr in left:
            res.append([root.val]+arr)

        return res


"""
- iterate leaves checking if they add up to the path sum
- if so, return an array of an array containing the leaf [[leaf,]]
    - and keep on adding the parent elements tto the array as you bubble up
    - if a parent has both of its children returning arrays, combine the inner arrays
    
    
"""

# -------------------------------------------------------------------------------------------------------------------------------------
