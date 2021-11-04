"""
Node Depths:
    The distance between a node in a Binary Tree and the tree's root is called the node's depth.
    Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.
    Each BinaryTree node has an integer value, a left child node, and a right child node.
    Children nodes can either be BinaryTree nodes themselves or None / null.
    
https://www.algoexpert.io/questions/Node%20Depths
"""


# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree
def nodeDepths(root,  depth=0):
    if root is None:
        return 0

    l = nodeDepths(root.left,  depth + 1)
    r = nodeDepths(root.right,  depth + 1)

    return depth + l + r


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
Sample Input
tree =    1
       /     \
       2      3
    /   \   /   \
   4     5 6     7
 /   \
8     9

1 + 2 + 3
Sample Output:
    16
    // The depth of the node with value 2 is 1.
    // The depth of the node with value 3 is 1.
    // The depth of the node with value 4 is 2.
    // The depth of the node with value 5 is 2.
    // Etc..
    // Summing all of these depths yields 16.


# Input: binary tree
# Output: sum_of_node_depths (int)
# Assumptions:
    BT is valid

#####
- figure out how to get depth for each node
- add all depths

# # First Approach:
# have a total variable
# recurse through all the nodes in the tree DFS/BFS - DFS in this case
    - passing in the current running depth
# at each node:
    if valid (not None):
        - current_running_depth += 1 (before we get there -> through the function)
        - repeat the above process for the left and right children then
             return the results + current_running_depth

# O(n) time | O(h) space


"""


def test():
    y = 1
    test2(y)
    print(y)


def test2(x):
    x = 22


test()


def nodeDepths2(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)
