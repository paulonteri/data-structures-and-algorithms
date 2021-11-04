"""
Binary Tree Inorder Traversal:

Given the root of a binary tree, return the inorder traversal of its nodes' values.

https://leetcode.com/problems/binary-tree-inorder-traversal/

https://www.enjoyalgorithms.com/blog/iterative-binary-tree-traversals-using-stack
https://www.educative.io/edpresso/how-to-perform-an-iterative-inorder-traversal-of-a-binary-tree
https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive

After this:
- https://leetcode.com/problems/binary-search-tree-iterator
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


""" 
 - add all left nodes to stack
 - visit left most node
 - move to the right
"""


class Solution_:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return None
        result = []

        stack = []
        curr = root
        while stack or curr:
            # add all left
            # put the left most value(s) to the top of the stack
            while curr and curr.left:
                stack.append(curr)
                curr = curr.left

            # the top of the stack has the left most unvisited value
            #  visit node
            if not curr:
                curr = stack.pop()
            result.append(curr.val)

            # - has no unvisited left
            # - itself is visited
            # so the next to be visited is right
            curr = curr.right

        return result


"""

class Solution:
    def inorderTraversal(self, root: TreeNode):
        output = []

        stack = []
        curr = root
        while curr is not None or len(stack) > 0:

            # add all left
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            # visit node
            temp = stack.pop()
            output.append(temp.val)

            curr = temp.right

        return output
"""


#         10
#       /    \
#      4      17
#    /   \      \
#   2     5     19
#  /           /
#  1           18

class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return None
        result = []

        stack = []
        curr = root
        while stack or curr:
            # put the left most value(s) to the top of the stack
            while curr:
                stack.append(curr)
                curr = curr.left

            # the top of the stack has the left most unvisited value
            #  visit node
            curr = stack.pop()
            result.append(curr.val)

            # - has no unvisited left
            # - itself is visited
            # so the next to be visited is right
            # eg: after 4 is 5 in the example above
            curr = curr.right

        return result


""" 
------------------------------------------------------------------------------------------------------------
"""


class Solution1:
    def inorderTraversal(self, root):
        output = []
        self.inorderTraversalHelper(root, output)
        return output

    def inorderTraversalHelper(self, root, output):
        if not root:
            return

        self.inorderTraversalHelper(root.left, output)
        output.append(root.val)
        self.inorderTraversalHelper(root.right, output)
