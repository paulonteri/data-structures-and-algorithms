"""
Find Closest Value In BST:

Write a function that takes in a Binary Search Tree (BST) and
 a target integer value and returns the closest value to that target value contained in the BST.
You can assume that there will only be one closest value.
Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
 its value is strictly greater than the values of every node to its left; its value is less than or
  equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.
  
https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST
"""


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(log(n)) time | O(1) space
# worst: O(n) time | O(1) space -> tree with one branch
def findClosestValueInBst(tree, target):
    curr = tree
    closest = float('inf')

    while curr is not None:

        # update closest
        if abs(curr.value-target) < abs(closest-target):
            closest = curr.value

        # move downwards
        if curr.left is None or (curr.right is not None and target >= curr.value):
            # target >= node.value: every value to the left will be further away from that target than the node.value
            curr = curr.right
        else:
            # target < node.value: every value to the right will be further away from that target than the node.value
            curr = curr.left

    return closest


"""
Sample Input
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
    target = 12

t = 12
    11
   / \
10    20

Sample Output
    13

# Input: tree & target
# Output: closest(int)

# # First Approach:
start at head
# at every node:
    - update closest value
    - target >= node.value: every value to the left will be further away from that target than the node.value
        - move to the right
    - target < node.value: every value to the right will be further away from that target than the node.value
        - move to the left
"""


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def findClosestValueInBst2(tree, target):
    closest = float('inf')
    curr = tree

    while curr is not None:

        # # update closest
        if abs(curr.value - target) < abs(closest - target):
            closest = curr.value

        # # move on to next node

        if curr.value == target:
            break  # no need to go on
        elif curr.value < target:
            # 05:55
            # because the curr node's value is less than the target,
            #   all values to the left of curr will be futher away from the target (BST property -> are less then curr)
            curr = curr.right
        else:
            # curr node's value is greater than the target, all values to the right of curr,
            #  will be further away from target as they are larger than curr
            curr = curr.left

    return closest
