""" 
Kth Largest Number in a Stream:


Design a class to efficiently find the Kth largest element in a stream of numbers.
The class should have the following two things:
    The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
    The class should expose a function add(int num) which will store the given number and return the Kth largest number.

Example 1:
    Input: [3, 1, 5, 12, 2, 11], K = 4
    1. Calling add(6) should return '5'.
    2. Calling add(13) should return '6'.
    2. Calling add(4) should still return '6'.
"""

""" 
Input: [3, 1, 5, 12, 2, 11], K = 4

sorted_input => [1,2,3,5,11,12]

1. Calling add(6) should return '5'.
[1,2,3,5,6,11,12]

2. Calling add(13) should return '6'.
[1,2,3,5,6,11,12,13]

2. Calling add(4) should still return '6'.
[1,2,3,4,5,6,11,12,13]

- if we find a way to store thr k largest numbers,
    we can be knowing the kth largest easily
- we can use a heap for this
"""




import heapq
class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def add(self, num):
        heapq.heappush(self.nums, num)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
