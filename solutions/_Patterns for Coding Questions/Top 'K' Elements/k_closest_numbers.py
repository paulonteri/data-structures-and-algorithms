"""
'K' Closest Numbers:

Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array.
Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:
		Input: [5, 6, 7, 8, 9], K = 3, X = 7
		Output: [6, 7, 8]
Example 2:
		Input: [2, 4, 5, 6, 9], K = 3, X = 6
		Output: [4, 5, 6]
Example 3:
		Input: [2, 4, 5, 6, 9], K = 3, X = 10
		Output: [5, 6, 9]
"""
import heapq

"""
SOLUTION;

O(N∗logK):
- for each number in the array, calculate its absolute difference with X
- store the difference in a max-heap(largest on top) maintaining K numbers in the heap
- return the heap

O(logN + KlogK)
- Since the array is sorted, we can first find the number closest to ‘X’ through Binary Search. Let’s say that number is ‘Y’.
- The ‘K’ closest numbers to ‘Y’ will be adjacent to ‘Y’ in the array. We can search in both directions of ‘Y’ to find the closest numbers.
- We can use a heap to efficiently search for the closest numbers. We will take ‘K’ numbers in both directions of ‘Y’
		and push them in a Min Heap sorted by their absolute difference from ‘X’.
		This will ensure that the numbers with the smallest difference from ‘X’ (i.e., closest to ‘X’) can be extracted easily from the Min Heap.
- Finally, we will extract the top ‘K’ numbers from the Min Heap to find the required numbers.
"""


# O(logN + KlogK) time | O(K) space
def find_closest_elements(arr, K, X):

    closest_idx = binary_search(arr, X)
    close = []
    for idx in range(max(0, closest_idx-K), min(len(arr), closest_idx+K+1)):
        num = arr[idx]
        heapq.heappush(close, [-abs(X-num), num])
        if len(close) > K:
            heapq.heappop(close)

    result = []
    for item in close:
        result.append(item[1])

    return result


def binary_search(arr, num):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left+right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            right = mid-1
        else:
            left = mid+1

    return left
