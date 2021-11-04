""" 
LinkedList Cycle:

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""

""" 
Imagine two racers running in a circular racing track. 
If one racer is faster than the other, the faster racer is bound to catch up and cross the slower racer from behind. 
We can use this fact to devise an algorithm to determine if a LinkedList has a cycle in it or not.
"""


def has_cycle(head):
    fast = head
    slow = head
    while fast != None:
        if fast == slow and fast != head:
            return True
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

    return False
