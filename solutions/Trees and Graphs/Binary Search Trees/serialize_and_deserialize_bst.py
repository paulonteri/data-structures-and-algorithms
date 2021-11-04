""" 
Serialize and Deserialize BST

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file 
    or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.

Example 1:
    Input: root = [2,1,3]
    Output: [2,1,3]
Example 2:
    Input: root = []
    Output: []

After this:
- https://leetcode.com/problems/serialize-and-deserialize-binary-tree

https://leetcode.com/problems/serialize-and-deserialize-bst
"""


""" 
Alternative solutions:
-  using preorder traversal (here we use postorder) https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single postorder string.
        """
        postorder_result = []

        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            postorder_result.append(node.val)

        postorder(root)
        return ' '.join(map(str,  postorder_result))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        def reverse_postorder(lower, upper):
            """ 
            Reverse of postorder: postorder is `lrn`, here we do `nrl`
            """
            if not data:
                return None
            if data[-1] < lower or data[-1] > upper:
                return None

            node = TreeNode(data.pop())
            node.right = reverse_postorder(node.val, upper)
            node.left = reverse_postorder(lower, node.val)

            return node

        data = [int(x) for x in data.split(' ') if x]
        return reverse_postorder(float('-inf'), float('inf'))


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
