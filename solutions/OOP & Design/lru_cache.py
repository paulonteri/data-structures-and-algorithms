"""
LRU Cache: Leecode 146

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?

https://leetcode.com/problems/lru-cache
"""

from collections import OrderedDict
from typing import Dict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


# special Doubly Linked List
class DLL:
    # head & tail will help in easily finding the beginning and end
    def __init__(self, head: Node, tail: Node):
        head.next = tail
        tail.prev = head
        self.head = head
        self.tail = tail

    def remove_between_head_and_tail(self, node: Node):
        # special remove function for our cache
        pr = node.prev
        nxt = node.next
        pr.next = nxt
        nxt.prev = pr

    def add_after_head(self, node: Node):
        after_head = self.head.next

        # update head
        self.head.next = node
        # update node that was after head
        after_head.prev = node
        # node
        node.next = after_head
        node.prev = self.head

    # ignore this
    # it is used for testing only
    def print_all(self):
        curr = self.head
        elements = []

        while curr is not None:
            pr = None
            nxt = None

            if curr.prev:
                pr = curr.prev
            if curr.next:
                nxt = curr.next
            elements.append([curr.key, curr.value, {"prev": pr, "next": nxt}])

        print(elements)
        return elements


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# SOLUTION:
# get O(1) time | put O(1)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        # used to store all the key value pairs
        self.store: Dict[int, Node] = {}
        # actual cache
        self.cache = DLL(Node(-1, -1), Node(-1, -1))

    def get(self, key: int):
        if not key in self.store:
            return -1
        else:
            node = self.store[key]
            # move to front (make most recent)
            self.cache.remove_between_head_and_tail(node)
            self.cache.add_after_head(node)
            return node.value

    def put(self, key: int, value: int):
        # have key in store
        if key in self.store:
            node = self.store[key]
            # update
            node.value = value
            # move to front (make most recent)
            self.cache.remove_between_head_and_tail(node)
            self.cache.add_after_head(node)
        # new key
        else:
            # create
            node = Node(key, value)
            self.store[key] = node
            self.cache.add_after_head(node)
            self.count += 1

        # check for excess
        if self.count > self.capacity:
            before_last = self.cache.tail.prev
            self.cache.remove_between_head_and_tail(before_last)
            self.store.pop(before_last.key)
            self.count -= 1


"""
Input:
    ["LRUCache","put","put","put","put","get","get"]
    [[2],       [2,1],[1,1],[2,3],[4,1],[1],   [2]]

    ["LRUCache","put","put","get","put","get","put","get","get","get"]
    [[2],      [1,10],[2,20],[1], [3,30],[2], [4,40],[1],  [3],[4]]
Output:
    [null,null,null,null,null,-1,3]

    [null,null,null,10,null,-1,null,-1,30,40]
"""


""" 
Ordered dictionary
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


class LRUCache2(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
