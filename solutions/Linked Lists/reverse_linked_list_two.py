"""
Reverse Linked List II:

Given the head of a singly linked list and two integers left and right where left <= right,
 reverse the nodes of the list from position left to position right, and return the reversed list.
Follow up: Could you do it in one pass?

Example 1:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]
Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]

https://leetcode.com/problems/reverse-linked-list-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        if left == right:
            return head

        before_sublist = after_sublist = None
        sublist_start = sublist_end = None

        prev = None
        curr = head
        count = 1
        while curr:
            if count == left-1:
                before_sublist = curr
            elif count == left:
                sublist_start = curr
            elif count == right:
                sublist_end = curr
            elif count == right+1:
                after_sublist = curr

            # reverse sublist
            nxt = curr.next
            if count > left and count <= right:
                curr.next = prev

            prev = curr
            curr = nxt
            count += 1

        # correct start and end of sublist
        if before_sublist is None:
            sublist_start.next = after_sublist
            return sublist_end  # new head
        else:
            before_sublist.next = sublist_end
            sublist_start.next = after_sublist
            return head


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        pos = 1

        curr = head
        prev = None

        #  # iterate till the position where we find the section to be reversed
        while pos < m:
            # move to next node
            prev = curr
            curr = curr.next

            pos += 1

        # store the last non reversed(not to be reversed) node
        last_none_reversed_node = prev
        # will be the tail of the last reversed list
        reversed_list_tail = curr

        #  # reverse a section of the list
        while pos <= n:
            nxt = curr.next

            # reverse pointer
            curr.next = prev

            # move on to next node
            prev = curr
            curr = nxt

            pos += 1

        # # fix the reversed list position in the larger list
        if last_none_reversed_node is not None:
            # last_none_reversed_node.next = last revered node
            last_none_reversed_node.next = prev
        # handle situation where we reversed from 1
        else:
            # if we started reversing from 1, then the last item reversed will be put at 1 (head)
            head = prev

        # connect the reversed list's tail to the the (n+1) node
        reversed_list_tail.next = curr

        return head


"""
Input:
    [1,2,3,4,5,6,7,8,9,10,11,12,13]
    3
    8
    [5]
    1
    1
    [3,5]
    1
    1
    [3,5]
    1
    2
Output:
    [1,2,8,7,6,5,4,3,9,10,11,12,13]
    [5]
    [3,5]
    [5,3]
"""


class Solution00:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        prev = None
        curr = head
        pos = 1

        # # find where reversing begins
        while pos < left:
            prev = curr
            curr = curr.next
            pos += 1
        # we cannot use before_reverse.next when left is at 1, coz there is no before_reverse so we use start_reverse
        start_reverse = curr
        before_reverse = prev

        # # reverse a section
        while pos <= right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            pos += 1

        # # merge the reversed section
        # the (left - 1) node to point to right
        if before_reverse and before_reverse.next:
            before_reverse.next = prev
        # if we started reversing at the head
        else:
            head = prev
        # the first reversed (left) node to point to the node at (right + 1)
        start_reverse.next = curr

        return head


"""
l = 3
r = 5
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

1 -> 2 -> <- 3  4 -> 5 -> 6 -> 7 -> 8 -> 9
curr = 3

1 -> 2 -> <- 3 <- 4 5 -> 6 -> 7 -> 8 -> 9
curr = 4

1 -> 2 -> <- 3 <- 4 <- 5 6 -> 7 -> 8 -> 9
curr = 5

"""


class Solution01:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        prev = None
        curr = head

        # # find where reversing begins
        for _ in range(left-1):  # the 1st node is at pos 1
            prev = curr
            curr = curr.next

        # we cannot use before_reverse.next when left is at 1, coz there is no before_reverse so we use start_reverse
        # store the last non reversed(not to be reversed) node
        start_reverse = curr
        # will be the tail of the last reversed list
        before_reverse = prev

        # # reverse a section
        for _ in range(left, right+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # # merge the reversed section (fix the reversed list position in the larger list)
        # the (left - 1) node to point to right
        if before_reverse and before_reverse.next:
            # before_reverse.next = last reversed node (prev)
            before_reverse.next = prev

        else:
            # if we started reversing from 1, then the last item reversed will be put at 1 (head)
            head = prev

        # the first reversed (left) node to point to the node at (right + 1)
        start_reverse.next = curr

        return head
