""" 
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example 1:
    1. insertNum(3)
    2. insertNum(1)
    3. findMedian() -> output: 2
    4. insertNum(5)
    5. findMedian() -> output: 3
    6. insertNum(4)
    7. findMedian() -> output: 3.5
https://www.educative.io/courses/grokking-the-coding-interview/3Yj2BmpyEy4
https://www.algoexpert.io/questions/Continuous%20Median
"""

"""
Solution:

Assume ‘x’ is the median of a list. This means that half of the numbers in the list will be smaller than (or equal to) ‘x’ and half will be greater than (or equal to) ‘x’.

- we basically have to keep track of the middle number(s) at every point

- we can divide the set of numbers into two sorted halves (small & large numbers)
    - the if total count of numbers is even, the median will be (the smallest large number + largest small number) / 2
    - otherwise the median will be the middle number

larger = []
smaller = []

1. insertNum(3)
larger = [3]
smaller = []

2. insertNum(1)
larger = [3]
smaller = [1]

3. findMedian() -> output: 2
(3+1)/2

4. insertNum(5)
larger = [3,5]
smaller = [1]

5. findMedian() -> output: 3
(3)

6. insertNum(4)
larger = [3,4,5]
smaller = [1]
---
larger = [4,5]
smaller = [3,1]


7. findMedian() -> output: 3.5
(3+4)/2

"""




import heapq
class MedianOfAStream:

    def __init__(self):
        self.smaller = []
        self.larger = []

    def insert_num(self, num):
        if len(self.larger) == 0 or num >= self.larger[0]:
            heapq.heappush(self.larger, num)
        else:
            heapq.heappush(self.smaller, -num)
        self.balance_heaps()

    def find_median(self):
        if len(self.larger) > len(self.smaller):
            return self.larger[0]
        else:
            return (self.larger[0] + -self.smaller[0]) / 2

    def balance_heaps(self):
        while len(self.larger) > len(self.smaller) + 1:
            heapq.heappush(self.smaller, -heapq.heappop(self.larger))
        while len(self.larger) < len(self.smaller):
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))


"""
Continuous Median:
Write a ContinuousMedianHandler class that supports:
The continuous insertion of numbers with the insert method.
The instant (O(1) time) retrieval of the median of the numbers that have been inserted thus far with the getMedian method.
The getMedian method has already been written for you. You simply have to write the insert method.
The median of a set of numbers is the "middle" number when the numbers are ordered from smallest to greatest. 
If there's an odd number of numbers in the set, as in {1, 3, 7}, the median is the number in the middle (3 in this case);
 if there's an even number of numbers in the set, as in {1, 3, 7, 8}, the median is the average of the two middle numbers ((3 + 7) / 2 == 5 in this case).

Sample Usage
// All operations below are performed sequentially.
ContinuousMedianHandler(): - // instantiate a ContinuousMedianHandler
    insert(5): -
    insert(10): -
    getMedian(): 7.5
    insert(100): -
    getMedian(): 10
https://www.algoexpert.io/questions/Continuous%20Median
"""


# import heapq

class ContinuousMedianHandlerBF:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.small_nums = []
        self.big_nums = []

    def insert(self, number):
        if len(self.small_nums) > 0 and -self.small_nums[0] > number:
            heapq.heappush(self.small_nums, -number)
        else:
            heapq.heappush(self.big_nums, number)
        self.balance_heaps()
        self.update_median()
        # self.print_heaps()

    def getMedian(self):
        return self.median

    def balance_heaps(self):

        while len(self.big_nums) - len(self.small_nums) >= 2:
            heapq.heappush(self.small_nums, -
                           heapq.heappop(self.big_nums))

        while len(self.small_nums) - len(self.big_nums) >= 1:
            heapq.heappush(self.big_nums, -
                           heapq.heappop(self.small_nums))

    def update_median(self):
        is_even = (len(self.big_nums) + len(self.small_nums)) % 2 == 0
        if is_even:
            self.median = (self.big_nums[0] + (-self.small_nums[0])) / 2
        else:
            self.median = self.big_nums[0]

    def print_heaps(self):
        print(self.small_nums, 'len: ', len(self.small_nums))
        print(self.big_nums, 'len: ', len(self.big_nums))
        print("\n")
