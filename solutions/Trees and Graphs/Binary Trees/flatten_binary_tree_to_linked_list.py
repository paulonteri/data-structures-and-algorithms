""" 
Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where 
    the right child pointer points to the next node in the list 
    and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

https://leetcode.com/problems/flatten-binary-tree-to-linked-list
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_:
    def flatten(self, root):
        if not root:
            return None

        if root.left:
            right = root.right
            # place the left subtree between the root & root.right
            root.right = root.left
            left_ending = self.flatten(root.left)
            left_ending.right = right

            # remove left
            root.left = None

        if root.right:
            return self.flatten(root.right)
        return root


"""
our algorithm will return the tail node of the flattened out tree.

For a given node, we will recursively flatten out the left and the right subtrees 
    and store their corresponding tail nodes in left_ending and right_ending respectively.

Next, we will make the following connections 
(only if there is a left child for the current node, else the left_ending would be null)
(Place the left subtree between the root & root.right)
    left_ending.right = node.right
    node.right = node.left
    node.left = None
 
Next we have to return the tail of the final, flattened out tree rooted at node. 
So, if the node has a right child, then we will return the right_ending, else, we'll return the left_ending
"""


class Solution1:
    def flatten(self, root):
        if not root:
            return None

        left_ending = self.flatten(root.left)
        right_ending = self.flatten(root.right)

        # If there was a left subtree, we shuffle the connections
        #   around so that there is nothing on the left side anymore.
        if left_ending:
            # Place the left subtree between the root & root.right
            left_ending.right = root.right
            root.right = root.left
            # Remove left
            root.left = None

        # We need to return the "rightmost" node after we are done wiring the new connections.
        # 2. For a node with only a left subtree, the rightmost node will be left_ending because it has been moved to the right subtree
        # 3. For a leaf node, we simply return the node
        return right_ending or left_ending or root


""" 
Using stack
"""


class Solution__:
    def flatten(self, root):
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            node.left = None
            if stack:
                node.right = stack[-1]  # Peek


""" 
O(1) Iterative Solution (Greedy & similar to Morris Traversal)
"""


class Solution:
    def flatten(self, root):
        if not root:
            return None

        curr = root
        while curr:

            # If there was a left subtree, we shuffle the connections
            #   around so that there is nothing on the left side anymore.
            if curr.left:
                l_right_most = self.find_right_most(curr.left)

                # place the left subtree between the root & root.right
                l_right_most.right = curr.right
                curr.right = curr.left

                # remove left
                curr.left = None

            curr = curr.right

    def find_right_most(self, root):
        curr = root
        while curr.right:
            curr = curr.right
        return curr
