"""
Sort K-Sorted Array:

Write a function that takes in a non-negative integer k and a k-sorted array of integers and
    returns the sorted version of the array. Your function can either sort the array in place
    or create an entirely new array.
A k-sorted array is a partially sorted array in which all elements are at most k positions away from their sorted position.
For example, the array [3, 1, 2, 2] is k-sorted with k = 3, because each element in the array is at most 3 positions away from its sorted position.
Note that you're expected to come up with an algorithm that can sort the k-sorted array faster than in O(nlog(n)) time.

Sample Input
    array = [3, 2, 1, 5, 4, 7, 6, 5]
    k = 3
Sample Output
    [1, 2, 3, 4, 5, 5, 6, 7]

https://www.algoexpert.io/questions/Sort%20K-Sorted%20Array
"""
import heapq

"""
 - have a min-heap with k elements

 - iterate through the input array and at each index:
    - remove and record the value at the top of the heap at the index
    - add the element at index + k to the heap
"""


# O(nlog(k)) time | O(k) space
def sortKSortedArray(array, k):

    # have a min-heap with k elements
    heap = array[:k+1]
    heapq.heapify(heap)

    for idx in range(len(array)):
        # remove and record the value at the top of the heap at the index
        array[idx] = heapq.heappop(heap)

        # add the element at index + k+1 to the heap
        if idx+k+1 < len(array):
            heapq.heappush(heap, array[idx+k+1])

    return array
