""" 
Linked List Cycle:

Given head, the head of a linked list, determine if the linked list has a cycle in it
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

https://leetcode.com/problems/linked-list-cycle
https://www.notion.so/paulonteri/Hare-Tortoise-Algorithm-1020d217ffb54e47b7aea3c175d75618#0f0930e961414b1e90871b4efbe3d1b6
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode):
        if head is None:
            return False

        slow = head
        # move fast
        fast = head.next
        if fast is None:
            return False
        fast = fast.next

        while fast != None:
            if fast == slow:
                return True

            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        return False
