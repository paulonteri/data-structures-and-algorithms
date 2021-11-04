""" 
Find start of linked list cycle:

Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
https://www.educative.io/courses/grokking-the-coding-interview/N7pvEn86YrN
https://www.notion.so/paulonteri/Hare-Tortoise-Algorithm-1020d217ffb54e47b7aea3c175d75618#0f0930e961414b1e90871b4efbe3d1b6
"""

"""
Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Notice that you should not modify the linked list
https://leetcode.com/problems/linked-list-cycle-ii/
https://www.algoexpert.io/questions/Find%20Loop
https://www.notion.so/paulonteri/Hare-Tortoise-Algorithm-1020d217ffb54e47b7aea3c175d75618#0f0930e961414b1e90871b4efbe3d1b6
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_start(head):
    cycle_length = 0
    # find the LinkedList cycle
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start(head, cycle_length)


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def find_start(head, cycle_length):
    pointer1 = head
    pointer2 = head

    # move pointer2 ahead 'cycle_length' nodes
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1

    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


class Solution:
    def detectCycle(self, head):
        if not head:
            return None

        # # find cycle
        fast = head
        slow = head
        while True:
            if fast is None or fast.next is None:  # find invalid
                return None

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # # find start of cycle
        # the (dist) head to the start of the cycle ==
        #   the (dist) meeting point to the start of the cycle
        one = head
        two = fast
        while one != two:
            one = one.next
            two = two.next
        return one


"""
Find Loop:
Write a function that takes in the head of a Singly Linked List that contains a loop 
(in other words, the list's tail node points to some node in the list instead of None / null). 
The function should return the node (the actual node--not just its value) from which the loop originates in constant space.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list.

Sample Input
    head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 0
                            ^         v
                            9 <- 8 <- 7
Sample Output
    4 -> 5 -> 6 // the node with value 4
    ^         v
    9 <- 8 <- 7
https://www.algoexpert.io/questions/Find%20Loop
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # .next to allow the first loop to work
    p_one = head.next
    p_two = head.next.next

    # find meeting point
    while p_two != p_one:
        p_one = p_one.next
        p_two = p_two.next.next

    # # find start of cycle
    # the (dist) head to the start of the cycle ==
    #   the (dist) meeting point to the start of the cycle
    p_one = head
    while p_two != p_one:
        p_one = p_one.next
        p_two = p_two.next

    return p_one
