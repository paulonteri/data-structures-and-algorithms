""" 
Rotate List/Shift Linked List:

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

Constraints:
    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

https://leetcode.com/problems/rotate-list/
https://www.algoexpert.io/questions/Shift%20Linked%20List
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- find length of list
- find end of list
- k %= length
- we'll have to pluck of the list from position length - k to the end
	and place it a the beginning of the list
	- get to node (length - k):
		- hold k in a pointer (new_head)
		- node (length - k) to point to null
		- end to point to head
	- return new_head


0 -> 1 -> 2 -> 3 -> 4 -> 5 

2
4 -> 5 -> 0 -> 1 -> 2 -> 3

5
1 -> 2 -> 3 -> 4 -> 5 -> 0


"""


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return

        # # get tail and length
        tail = None
        length = 0
        curr = head
        while curr:
            tail = curr
            curr = curr.next
            length += 1

        # # validate k
        k %= length
        if k == 0:
            return head

        # # find new ending (length - k)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # # rotate
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
