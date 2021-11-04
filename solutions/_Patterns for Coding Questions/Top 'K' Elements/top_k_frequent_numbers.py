""" 
Top 'K' Frequent Numbers:

Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:
    Input: [1, 3, 5, 12, 11, 12, 11], K = 2
    Output: [12, 11]
    Explanation: Both '11' and '12' appeared twice.
Example 2:
    Input: [5, 12, 11, 3, 11], K = 2
    Output: [11, 5] or [11, 12] or [11, 3]
    Explanation: Only '11' appeared twice, all other numbers appeared once.
"""
from typing import List

from collections import Counter
from heapq import heappop, heappush


""" 
- have a min heap (smallest number at the top)
- get the count of all nums in the array
- all the counts plus corresponding numbers to the heap
    - the heap will contain a max of k elements
- return the numbers in the heap
"""


# O(N∗logK) time | O(N) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        min_heap = []

        for number, count in Counter(nums).items():
            heappush(min_heap, (count, number))
            if len(min_heap) > k:
                heappop(min_heap)

        return [item[1] for item in min_heap]
