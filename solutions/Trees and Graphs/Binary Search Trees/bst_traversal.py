"""
BST Traversal:

Write three functions that take in a Binary Search Tree (BST) and an empty array,
 traverse the BST, add its nodes' values to the input array, and return that array.
The three functions should traverse the BST using the in-order, pre-order, and post-order tree-traversal techniques, respectively.

Each BST node has an integer value, a left child node, and a right child node.
A node is said to be a valid BST node if and only if it satisfies the BST property:
 its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right;
  and its children nodes are either valid BST nodes themselves or None / null.

https://www.algoexpert.io/questions/BST%20Traversal
"""

# In  ->  lnr
# Pre ->  nlr
# Post -> lrn


def inOrderTraverse(node, array):
    if node is None:
        return

    # before we get to the append we inOrderTraverse() on the left, then we find anther left, we inOrderTraverse on the left again and again
    #  till we are at the final left for a given tree/sub-tree
    # we finally append its value then call inOrderTraverse() on its right child and the process repeats istself again and again

    # we will keep on going till the furthest left before any other step like array.append(node.value) or inOrderTraverse(node.right, array)
    inOrderTraverse(node.left, array)
    array.append(node.value)
    inOrderTraverse(node.right, array)

    return array


def preOrderTraverse(node, array):
    if node is None:
        return

    array.append(node.value)
    preOrderTraverse(node.left, array)
    preOrderTraverse(node.right, array)

    return array


def postOrderTraverse(node, array):
    if node is None:
        return

    postOrderTraverse(node.left, array)
    postOrderTraverse(node.right, array)
    array.append(node.value)

    return array
