"""
Binary Search Tree Iterator:

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1:
     7
    / \
    3  15
       / \
       9  20
    Input
    ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
    [null, 3, 7, true, 9, true, 15, true, 20, false]

    Explanation
    BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
    bSTIterator.next();    // return 3
    bSTIterator.next();    // return 7
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 9
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 15
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 20
    bSTIterator.hasNext(); // return False
"""

from typing import Optional
""" 
----
Solution 1:
store the inorder traversal in an array and return them index by index

---
Solution 2:
controlled iteration

check Binary Tree Inorder Traversal (Iterative)
https://www.notion.so/paulonteri/Trees-Graphs-edc3401e06c044f29a2d714d20ffe185#8c489e8b02804929ab535f25f945a31b

[3,7,9,15,20]


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = root
        self.stack = []

    def next(self):
        # put the left most value(s) to the top of the stack
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        # the left-most node is at the top of the stack
        node = self.stack.pop()
        # the next (only next unvisited valid node) will be at the right
        self.curr = node.right

        return node.val

    def hasNext(self):
        return self.curr or self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
