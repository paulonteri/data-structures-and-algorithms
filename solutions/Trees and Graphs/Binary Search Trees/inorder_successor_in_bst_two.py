""" 
510. Inorder Successor in BST II

Given a node in a binary search tree, return the in-order successor of that node in the BST. 
If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. 
Each node will have a reference to its parent node. Below is the definition for Node:
    class Node {
        public int val;
        public Node left;
        public Node right;
        public Node parent;
    }

https://leetcode.com/problems/inorder-successor-in-bst-ii
https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#a6523a68c7ec4a19bfe6923d7e051797
"""

""" 
Node has a right child, and hence its successor is somewhere lower in the tree. 
To find the successor, go to the right once and then as many times to the left as you could.

Node has no right child, then its successor is somewhere upper in the tree. 
To find the successor, go up till the node that is left child of its parent. The answer is the parent. 
Beware that there could be no successor (= null successor) in such a situation.
"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def inorderSuccessor(self, node):
        curr = node

        if curr.right:
            # get left most child in right subtree
            curr = curr.right
            while curr and curr.left:
                curr = curr.left
            return curr

        else:
            # find where the tree last branched left
            while curr:
                if curr.parent and curr.parent.left == curr:
                    return curr.parent
                curr = curr.parent

        return None
