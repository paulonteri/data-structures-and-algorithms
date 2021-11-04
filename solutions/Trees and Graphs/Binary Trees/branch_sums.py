"""
Branch Sums:

Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.
A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.
Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None / null.

https://www.algoexpert.io/questions/Branch%20Sums
"""


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(d) space
def branchSums(root):
    sums = []
    branchSumsHelper(root, 0, sums)
    return sums


def branchSumsHelper(root, running_sum, sums):
    if root is None:
        return

    running_sum += root.value  # increase running sum

    if root.left is None and root.right is None:  # leaf node
        sums.append(running_sum)
        return

    branchSumsHelper(root.left, running_sum, sums)
    branchSumsHelper(root.right, running_sum, sums)


"""
# Input: binary tree
    - valid BT
# Output: Array of Integers
# Assumptions:
    - All nodes will be valid
    - BT will have at least one node


# Simple Examples:
tree =     1
1      /     \
       2       3
result = (1+2) + (1+3) = 7

tree =     1
1      /     \
3     2    4  3
     /   \    /11 \
    4     5  6    7
  /   \  /
 8    9 10

(1+2+4+8) = 15
(1+2+4+9) = 16
(1+2+5+10) = 18
...

## Need to figure out
- how to incriment the sum downwards
- how to pass the total branch sums back upwards 
- when we are on a leaf node

# # First Solution: 
# Recurse through the tree in DFS & inOrderTraversal
# For every node, return the sum of its branch sums (left_branch_sum + right_branch_sum)

# example:
def branchSums(root, running_sum=0, sums=[]):
    if root is None:
        return

    running_sum += node.value
    if root.left is None and root.right is None:
        sums.append(running_sum)
        return

    
    branchSums(root.left, running_sum, sums)
    branchSums(root.right, running_sum, sums)
    


# O(n) time | O(d) space
where n is the number of nodes in the tree
where d is the depth/height of the deepest leaf

"""
