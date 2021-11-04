"""
Intersection of Two Linked Lists:

Write a program to find the node at which the intersection of two singly linked lists begins.
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):

        A_visited = {}
        while headA is not None:
            A_visited[headA] = True
            headA = headA.next
        while headB is not None:
            if headB in A_visited:
                return headB
            headB = headB.next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):

        ## LOGIC ##
        # 1) Find the length of both lists;
        # 2) In the biggest list, advance its head N times where N is the length difference between the two lists.
        # 3) Now both lists have the same length, just iterate them and check for node equality.

        ## TIME COMPLEXITY : O(M+N) ##
        ## SPACE COMPLEXITY : O(1) ##

        a = headA
        b = headB

        len_a = 0
        len_b = 0
        while a is not None or b is not None:  # find lengths
            if a:
                len_a += 1
                a = a.next
            if b:
                len_b += 1
                b = b.next

        if len_a > len_b:
            longer = headA
            shorter = headB
        else:
            longer = headB
            shorter = headA

        counter = abs(len_a-len_b)
        while longer is not None and counter > 0:
            longer = longer.next
            counter -= 1

        while longer is not None or shorter is not None:  # find lengths
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next

        return None
