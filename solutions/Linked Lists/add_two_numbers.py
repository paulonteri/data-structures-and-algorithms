"""
Add Two Numbers: Leetcode 2

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    """
    This is how addition works (Elementary Math):

      111 <- carried values
      |||
     7692
    +3723
    -----
     0426
    -----
    """

    # O(max(m,n)) time | O(max(m,n)) space | m=len(l1), n=len(l2)
    def addTwoNumbers(self, l1, l2):

        # declare pointers
        p1 = l1
        p2 = l2

        # used to store the carry value
        carry = 0

        # declare result linked list
        result = ListNode()
        res_curr = result  # position on the result linked list

        # remember to add the 'carry' edge case to the while loop
        # example 119 + 119
        while p1 != None or p2 != None or carry != 0:

            top = 0
            bottom = 0

            if p1 != None:
                top = p1.val
                p1 = p1.next

            if p2 != None:
                bottom = p2.val
                p2 = p2.next

            my_sum = carry + top + bottom

            # check if we'll carry
            # max of my_sum is 19
            if my_sum > 9:  # carry value
                res_curr.next = ListNode(val=my_sum-10)
                carry = 1
            else:
                res_curr.next = ListNode(val=my_sum)
                carry = 0

            res_curr = res_curr.next

        # skip the node we created during initialization of the linked list
        return result.next
