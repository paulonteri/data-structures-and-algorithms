"""
Length of LinkedList Cycle:

Given the head of a LinkedList with a cycle, find the length of the cycle.
"""

"""
Once the fast and slow pointers meet,
 we can save the slow pointer and iterate the whole cycle with another pointer
 until we see the slow pointer again to find the length of the cycle.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            return calculate_cycle_length(slow)

    return 0


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length
