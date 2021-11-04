"""
Copy List with Random Pointer:

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

https://leetcode.com/problems/copy-list-with-random-pointer/
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node'):

        # create new nodes
        node = head
        while node:
            node.random = Node(node.val, None, node.random)
            node = node.next

        # populate random field of the new node
        node = head
        while node:
            new_node = node.random
            new_node.random = new_node.random.random if new_node.random else None
            node = node.next

        # restore original list and build new list
        head_copy, node = head.random if head else None, head
        while node:
            node.random.next = node.next.random if node.next else None
            node.random = node.random.next
            node = node.next
        return head_copy


""" 
"""


class Solution_:
    def copyRandomList(self, head):

        result = Node(-1)

        curr = result
        store = {}
        while head is not None:
            # create node
            if head not in store:
                new_node = Node(head.val)
                store[head] = new_node  # add node to store
            else:
                new_node = store[head]

            # create random
            if head.random is not None:
                if head.random not in store:
                    new_random = Node(head.random.val)
                    new_node.random = new_random
                    store[head.random] = new_random  # add node to store
                else:
                    new_node.random = store[head.random]

            # next
            curr.next = new_node
            curr = new_node

            head = head.next

        return result.next


class Solution00:
    def getOrCreateNodeCopy(self, store, node):
        # we store the original node as a key and,
        #   the new node (copy) as its value
        if node not in store:
            store[node] = Node(node.val)

        return store[node]

    def copyRandomList(self, head: 'Node'):
        res = Node(-1)
        store = {}
        copy = res
        old = head
        while old is not None:
            # create old & old.random copies
            node = self.getOrCreateNodeCopy(store, old)
            if old.random is not None:
                node.random = self.getOrCreateNodeCopy(store, old.random)

            copy.next = node
            copy = node

            old = old.next

        return res.next
