""" 
Quick Select:
pre: Quick Sort

Pick a random number from the input array (the first number, for instance) and let that number be the pivot. 
Iterate through the rest of the array using two pointers, one starting at the left extremity of the array and progressively moving to the right, 
    and the other one starting at the right extremity of the array and progressively moving to the left. 
As you iterate through the array, compare the left and right pointer numbers to the pivot. 
If the left number is greater than the pivot and the right number is less than the pivot, swap them; this will effectively sort these numbers with respect to the pivot at the end of the iteration. 
If the left number is ever less than or equal to the pivot, increment the left pointer; similarly, if the right number is ever greater than or equal to the pivot, decrement the right pointer. 
Do this until the pointers pass each other, at which point swapping the pivot with the right number should position the pivot in its final, sorted position, 
    where every number to its left is smaller and every number to its right is greater.

If the pivot is in the kth position, you're done; if it isn't, figure out if the kth smallest number is located to the left or to the right of the pivot.
Repeat the process on the side of the kth smallest number, and keep on repeating the process thereafter until you find the answer.

https://www.algoexpert.io/questions/Quickselect
https://leetcode.com/problems/kth-largest-element-in-an-array
"""


def quickselect(array, k):
    return quick_select_helper(array, k-1, 0, len(array)-1)


def quick_select_helper(array, idx, start, end):
    if start == end:
        return array[start]

    pivot = start
    # # sort numbers with respect to pivot then put pivot between the large and small numbers
    #   left and right to stop at a place where: left >= pivot & right <= pivot
    left = pivot+1
    right = end
    while left <= right:
        # can be swapped
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]

        if array[left] <= array[pivot]:  # no need to swap
            left += 1
        if array[right] >= array[pivot]:  # no need to swap
            right -= 1

    # # place the pivot at correct position (right)
    # # place pivot at correct position
    # we know that once the sorting is done, the number at left >= pivot & right <= pivot
    #   smaller values go to the left of array[pivot]
    array[pivot], array[right] = array[right], array[pivot]
    if right == idx:
        return array[right]

    # # proceed search
    if idx < right:
        return quick_select_helper(array, idx, start, right-1)
    else:
        return quick_select_helper(array, idx, right+1, end)
