""" 
Top 'K' Numbers:

Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Example 1:
    Input: [3, 1, 5, 12, 2, 11], K = 3
    Output: [5, 12, 11]
Example 2:
    Input: [5, 12, 11, -1, 12], K = 3
    Output: [12, 11, 12]
"""

import heapq
""" 
Solution:

get rid of all smaller numbers

A brute force solution could be to sort the array and return the largest K numbers. 
The time complexity of such an algorithm will be O(N*logN) as we need to use a sorting algorithm.

If we iterate through the array one element at a time and keep ‘K’ largest numbers in a heap such that
 each time we find a larger number than the smallest number in the heap, we do two things:
    - Take out the smallest number from the heap, and
    - Insert the larger number into the heap.
This will ensure that we always have ‘K’ largest numbers in the heap. 

As discussed above, 
 it will take us O(logK) to extract the minimum number from the min-heap. 
So the overall time complexity of our algorithm will be O(K*logK+(N-K)*logK) since, 
 first, we insert ‘K’ numbers in the heap and then iterate through the remaining numbers and at every step, 
 in the worst case, we need to extract the minimum number and insert a new number in the heap. 
This algorithm is better than O(N*logN).
"""


# import heapq

# O(N∗logK) time | O(K) space
def find_k_largest_numbers(nums, k):
    res = []
    for num in nums:
        heapq.heappush(res, num)
        while len(res) > k:
            heapq.heappop(res)
    return res
