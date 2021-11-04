""" 
116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
    struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
    }

Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

https://leetcode.com/problems/populating-next-right-pointers-in-each-node
EPI 9.16
"""
import collections


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node'):
        if not root:
            return

        queue = [root]
        while queue:
            curr = queue.pop(0)

            if curr.left:
                curr.left.next = curr.right
                queue.append(curr.left)

            if curr.right:
                if curr.next:
                    curr.right.next = curr.next.left
                queue.append(curr.right)

        return root


""" 
"""


class Solution_:
    def connect(self, root: 'Node'):
        if not root:
            return None

        prev_nodes = collections.defaultdict(lambda: None)
        queue = [(root, 0)]

        while queue:
            curr, depth = queue.pop(0)

            curr.next = prev_nodes[depth]
            prev_nodes[depth] = curr

            # next
            if curr.right:
                queue.append((curr.right, depth+1))
            if curr.left:
                queue.append((curr.left, depth+1))

        return root
