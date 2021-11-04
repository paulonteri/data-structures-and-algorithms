""" 
Insert into a Sorted Circular Linked List:

Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.
If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.
If the list is empty (i.e., the given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

Example 1:
    Input: head = [3,4,1], insertVal = 2
    Output: [3,4,1,2]
    Explanation: In the figure above, there is a sorted circular list of three elements. 
                    You are given a reference to the node with value 3, and we need to insert 2 into the list. 
                    The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
Example 2:
    Input: head = [], insertVal = 1
    Output: [1]
    Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
Example 3:
    Input: head = [1], insertVal = 0
    Output: [1,0]

https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int):
        node = Node(insertVal)

        # empty list
        if not head:
            node.next = node
            return node

        smallest = head
        largest = head
        curr = head.next
        while curr != head:
            # the or equal is to ensure the largest is the last node in such [3,3,3]
            if curr.val < smallest.val:
                smallest = curr
            if curr.val >= largest.val:
                largest = curr
            curr = curr.next

        # only one node or all nodes have a similar value
        if smallest.val == largest.val:
            largest.next = node
            node.next = smallest

        # is the largest or smallest value
        elif insertVal <= smallest.val or insertVal >= largest.val:
            largest.next = node
            node.next = smallest

        else:
            prev = None
            curr = None
            while curr != smallest:
                if curr is None:
                    curr = smallest
                    prev = largest

                if insertVal < curr.val:
                    prev.next = node
                    node.next = curr
                    break

                prev = curr
                curr = curr.next

        return head
