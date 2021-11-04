"""
Kth Smallest Number in M Sorted Lists:

Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:
    Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
    Output: 4
    Explanation: The 5th smallest number among all the arrays is 4, this can be verified from
        the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:
    Input: L1=[5, 8, 9], L2=[1, 7], K=3
    Output: 7
    Explanation: The 3rd smallest number among all the arrays is 7.
"""


"""
L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5

- initialise heap with the first element of each list
- pop the smallest element from the heap and replace it with the next element from the list it came from
    - repeat until the K'th time and return the number
"""




import heapq
class HeapElement:
    def __init__(self, val, val_idx, list_idx):
        self.val = val
        self.val_idx = val_idx
        self.list_idx = list_idx

    def __gt__(self, other):
        return self.val > other.val

    def get_list(self, arr):
        return arr[self.list_idx]


def find_Kth_smallest(lists, k):

    heap = []
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            heapq.heappush(heap, HeapElement(lists[i][0], 0, i))

    number = -1
    for _ in range(k):
        if len(heap) == 0:
            return -1
        smallest = heapq.heappop(heap)

        # record number
        number = smallest.val

        # replace with next element from the list
        if smallest.val_idx + 1 < len(smallest.get_list(lists)):
            element = HeapElement(
                smallest.get_list(lists)[smallest.val_idx + 1],
                smallest.val_idx + 1,
                smallest.list_idx
            )
            heapq.heappush(heap, element)
    return number


print("Kth smallest number is: " +
      str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
print("Kth smallest number is: " +
      str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 2)))
print("Kth smallest number is: " +
      str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 1)))
print("Kth smallest number is: " +
      str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 200)))
