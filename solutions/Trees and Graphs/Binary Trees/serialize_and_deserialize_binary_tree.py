""" 
Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
    or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]
Example 2:
    Input: root = []
    Output: []
Example 3:
    Input: root = [1]
    Output: [1]
Example 4:
    Input: root = [1,2]
    Output: [1,2]

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Prerequisites:
- https://leetcode.com/problems/serialize-and-deserialize-bst
- https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        preorder_result = []

        # def preorder(node):
        #     if not node:
        #         preorder_result.append(str(None))
        #         return

        #     preorder_result.append(str(node.val))
        #     preorder(node.left)
        #     preorder(node.right)
        def preorder(node):
            if not node:
                preorder_result.append(str(None))
                return

            preorder_result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(preorder_result)

    def deserialize(self, data):
        idx = 0

        def reverse_preorder(arr):
            nonlocal idx
            if idx > len(arr):
                return None
            if arr[idx] == 'None':
                idx += 1
                return None

            node = TreeNode(int(arr[idx]))
            idx += 1

            node.left = reverse_preorder(arr)
            node.right = reverse_preorder(arr)

            return node

        return reverse_preorder(data.split(" "))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
