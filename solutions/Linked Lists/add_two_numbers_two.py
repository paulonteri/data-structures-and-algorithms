"""
Add Two Numbers II:

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

https://leetcode.com/problems/add-two-numbers-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 0(max(n+m)) time | 0(n+m) space
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):

        result = ListNode(-1)

        stack_one = []
        stack_two = []

        # fill up the stacks
        item_one = l1
        while item_one:
            stack_one.append(item_one.val)
            item_one = item_one.next
        item_two = l2
        while item_two:
            stack_two.append(item_two.val)
            item_two = item_two.next

        len_one = len(stack_one)
        len_two = len(stack_two)
        max_len = max(len_one, len_two)

        # addition
        i = 0
        carry = 0
        node_after_head = None
        while i <= max_len:  # iterate till max_len in order to handle carries

            # get values
            val_one = 0
            if i < len_one:
                val_one = stack_one.pop()
            val_two = 0
            if i < len_two:
                val_two = stack_two.pop()

            # arithmetic
            total = val_one + val_two + carry
            carry = 0
            if total > 9:
                total -= 10  # eg: when total = 19 : add (19-10) and carry 1
                carry = 1

            # add nodes to the result
            # if we are still adding or we have one left carry(eg: 99 + 99)
            if i < max_len or total > 0:
                node = ListNode(total)
                if node_after_head:
                    node.next = node_after_head
                    result.next = node
                    node_after_head = node
                else:
                    result.next = node
                    node_after_head = node
            i += 1

        # skip the first node (start at node_after_head)
        return result.next


"""
Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

input:
    [7,2,4,3]
    [5,6,4]
    [9,8,7,6,6,7,8,9]
    [9,8,7,6,6,7,8,9]
    [1,2,3,4,5,5,6,9]
    [1,2,3,4,5,5,6,9]
output:
    [7,8,0,7]
    [7,8,0,7]
    [1,9,7,5,3,3,5,7,8]
    [2,4,6,9,1,1,3,8]
    [1,5]
"""


class Solution00:
    def reverseLinkedList(self, head):
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        one = self.reverseLinkedList(l1)
        two = self.reverseLinkedList(l2)

        res = ListNode()
        curr = res
        carry = 0
        while one is not None or two is not None or carry > 0:
            total = carry
            carry = 0
            if one is not None:
                total += one.val
                one = one.next
            if two is not None:
                total += two.val
                two = two.next

            curr.next = ListNode(total % 10)
            curr = curr.next
            carry = total // 10

        return self.reverseLinkedList(res.next)


class Solution01:

    def stackFromLinkedList(self, head):
        stack = []
        curr = head
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next

        return stack

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        res = ListNode()
        node_after_res = None

        stack_one = self.stackFromLinkedList(l1)
        stack_two = self.stackFromLinkedList(l2)

        carry = 0
        idx, len_one, len_two = 0, len(stack_one), len(stack_two)
        while idx < len_one or idx < len_two or carry > 0:
            total = carry
            if idx < len_one:
                total += stack_one.pop()
            if idx < len_two:
                total += stack_two.pop()

            carry = total // 10

            # make sure node comes between res & node_after_res,
            #  making it the new node_after_res
            node = ListNode(total % 10)
            if node_after_res:
                node.next = node_after_res
            res.next = node
            node_after_res = node

            idx += 1

        return res.next


""" 
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

h -> 7
h -> 0 -> 7
h -> 8 -> 0 -> 7
"""
