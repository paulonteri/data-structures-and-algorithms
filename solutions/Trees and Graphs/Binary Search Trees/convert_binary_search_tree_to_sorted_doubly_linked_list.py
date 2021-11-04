""" 
Convert Binary Search Tree to Sorted Doubly Linked List:

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. 
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, 
 and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

            4
           / \
          2   5
         / \
        1   3
        
        
        1 2 3 4 5

https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list
"""


"""

            4
           / \
          2   5
         / \
        1   3
        
        
        1 2 3 4 5
        
        
        
prev = None
curr = 1
---
prev = 1
curr = 2

prev.right = curr
curr.left = prev


 r -->  <-- l r -->  <-- l 
1            2           3
---
prev = 2
curr = 3

2.right = 3
3.left = 2
  
O(tree depth), so O(n) worst case and O(log(n)) space
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return

        first, last = None, None

        stack = []
        curr, prev = root, None
        while curr or stack:
            # # Inorder traversal
            while curr and curr.left:
                stack.append(curr)
                curr = curr.left
            if not curr:
                curr = stack.pop()

            # # Linked List operations
            if prev:
                prev.right = curr
            curr.left = prev
            #
            if not first:
                first = curr
            last = curr
            prev = curr

            # # move to next
            curr = curr.right

        # # Linked List operations
        last.right = first
        first.left = last

        return first


""" 
"""


class TreeInfo:
    def __init__(self):
        self.smallest = None
        self.prev = None
        self.largest = None


class Solution_:
    def treeToDoublyList(self, root: 'Node'):
        tree_info = TreeInfo()
        self.in_order_traversal(root, tree_info)

        if tree_info.smallest and tree_info.largest:
            tree_info.smallest.left = tree_info.largest
            tree_info.largest.right = tree_info.smallest

        return tree_info.smallest

    def in_order_traversal(self, root, tree_info):
        if not root:
            return

        self.in_order_traversal(root.left, tree_info)

        # visit node
        if tree_info.smallest is None:  # first node
            tree_info.smallest = root
            tree_info.prev = root
            tree_info.largest = root
        else:
            # pointers
            tree_info.prev.right = root
            root.left = tree_info.prev
            # update info
            tree_info.prev = root
            tree_info.largest = root

        self.in_order_traversal(root.right, tree_info)
