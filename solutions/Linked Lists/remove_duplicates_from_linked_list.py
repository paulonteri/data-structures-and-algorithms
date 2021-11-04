"""
Remove Duplicates From Linked List:

You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.
Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values.

The Linked List should be modified in place (i.e., you shouldn't create a brand new list), and the modified Linked List should still have its nodes sorted with respect to their values.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.
https://www.algoexpert.io/questions/Remove%20Duplicates%20From%20Linked%20List
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    prev = linkedList
    curr = linkedList.next

    while curr is not None:
        if prev.value == curr.value:  # remove duplicate
            curr = curr.next
            prev.next = curr

        else:
            prev = curr
            curr = curr.next

    return linkedList


# O(n) time | O(1) space
def removeDuplicatesFromLinkedList2(linkedList):
    curr = linkedList

    while curr is not None:
        next_distinct_node = curr.next

        # skip duplicates
        while next_distinct_node is not None and next_distinct_node.value == curr.value:
            next_distinct_node = next_distinct_node.next
        curr.next = next_distinct_node

        # move forward
        curr = curr.next

    return linkedList
