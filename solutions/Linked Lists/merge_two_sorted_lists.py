"""
Merge Two Sorted Lists/Merge Linked Lists:

Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

https://www.algoexpert.io/questions/Merge%20Linked%20Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        one = l1
        two = l2

        # deal with head (larger one to be two and head)
        if one.val < two.val:
            temp_one = one
            one = two
            two = temp_one
        head = two

        prev_two = None
        # add one into two
        while one is not None and two is not None:
            if one.val < two.val:
                nxt = one.next
                self.insertBetween(prev_two, two, one)
                prev_two = one
                one = nxt
            else:
                prev_two = two
                two = two.next

        while one is not None:  # add remaining one into two
            prev_two.next = one
            prev_two = prev_two.next
            one = one.next

        return head

    def insertBetween(self, left, right, new):
        left.next = new
        new.next = right
