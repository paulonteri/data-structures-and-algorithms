""" 
Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

https://leetcode.com/problems/kth-largest-element-in-an-array
"""


class Solution:
    def findKthLargest(self, array, k):
        return self.quick_select(array, len(array)-k, 0, len(array)-1)

    def quick_select(self, array, idx, start, end):
        if start == end:
            return array[start]

        # # pick pivot and sort numbers relative to it (like quick sort)
        pivot = start
        # # sort numbers with respect to pivot then put pivot between the large and small numbers
        #   left and right to stop at a place where: left >= pivot & right <= pivot
        left = start + 1
        right = end
        while left <= right:
            # check if can be swapped
            if array[left] > array[pivot] and array[right] < array[pivot]:
                array[left], array[right] = array[right], array[left]

            if array[left] <= array[pivot]:  # no need to swap
                left += 1
            if array[right] >= array[pivot]:  # no need to swap
                right -= 1

        # place pivot at correct position
        # # place the pivot at correct position (right)
        # # place pivot at correct position
        # we know that once the sorting is done, the number at left >= pivot & right <= pivot
        #   smaller values go to the left of array[pivot]
        # # right is at a value < pivot, so ot should be moved left
        array[pivot], array[right] = array[right], array[pivot]

        # after swapping right is the only number we are sure is sorted
        # check if we are at the idx being looked for
        if right == idx:
            return array[right]

        # # proceed search
        elif right < idx:
            return self.quick_select(array, idx, right+1, end)
        else:
            return self.quick_select(array, idx, start, right-1)


x = Solution()
x.findKthLargest([5, 6, 4], 2)
