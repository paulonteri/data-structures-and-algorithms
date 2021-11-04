"""
Min Max Stack Construction:

Write a MinMaxStack class for a Min Max Stack. The class should support:
Pushing and popping values on and off the stack.
Peeking at the value at the top of the stack.
Getting both the minimum and the maximum values in the stack at any given point in time.
All class methods, when considered independently, should run in constant time and with constant space.

Sample Usage:
    // All operations below are performed sequentially.
    MinMaxStack(): - // instantiate a MinMaxStack
    push(5): -
    getMin(): 5
    getMax(): 5
    peek(): 5
    push(7): -
    getMin(): 5
    getMax(): 7
    peek(): 7
    push(2): -
    getMin(): 2
    getMax(): 7
    peek(): 2
    pop(): 2
    pop(): 7
    getMin(): 5
    getMax(): 5
    peek(): 5

https://www.algoexpert.io/questions/Min%20Max%20Stack%20Construction
"""


# all of the following will be called at valid times
class MinMaxStack:
    def __init__(self):
        self.store = []
        # stores our min & max for every value in the stack. history/archive
        self.min_max_store = []

    def peek(self):
        return self.store[-1]

    def pop(self):
        self.min_max_store.pop()
        return self.store.pop()

    def push(self, number):
        self.store.append(number)

        # store the current max & min
        max_value = number
        min_value = number
        if len(self.min_max_store) > 0:
            max_value = max(number, self.getMax())
            min_value = min(number, self.getMin())
        self.min_max_store.append({
            "max": max_value,
            "min": min_value
        })

    def getMin(self):
        return self.min_max_store[-1]['min']

    def getMax(self):
        return self.min_max_store[-1]['max']
