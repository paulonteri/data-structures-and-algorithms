""" 
622. Design Circular Queue:

Design your implementation of the circular queue. 
The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle 
    and the last position is connected back to the first position to make a circle. 
It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. 
But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:
    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 


Example 1:
    Input
        ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
        [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Output
        [null, true, true, true, false, 3, true, true, true, 4]
    Explanation
        MyCircularQueue myCircularQueue = new MyCircularQueue(3);
        myCircularQueue.enQueue(1); // return True
        myCircularQueue.enQueue(2); // return True
        myCircularQueue.enQueue(3); // return True
        myCircularQueue.enQueue(4); // return False
        myCircularQueue.Rear();     // return 3
        myCircularQueue.isFull();   // return True
        myCircularQueue.deQueue();  // return True
        myCircularQueue.enQueue(4); // return True
        myCircularQueue.Rear();     // return 4
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.store = [None] * k
        self.start = 0
        self.items_count = 0

    def enQueue(self, value: int):
        if self.isFull():
            return False

        if self.isEmpty():
            self.store[self.start] = value
        else:
            next_idx = self._getEndIdx() + 1
            next_idx %= len(self.store)
            self.store[next_idx] = value

        self.items_count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.store[self.start] = None
        self.start += 1
        self.start %= len(self.store)

        self.items_count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.store[self.start]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.store[self._getEndIdx()]

    def isEmpty(self):
        return self.items_count == 0

    def isFull(self):
        return self.items_count == len(self.store)

    def _getEndIdx(self):
        return (self.start + self.items_count - 1) % len(self.store)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
