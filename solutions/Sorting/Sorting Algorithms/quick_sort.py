""" 
Quick Sort:

Quick Sort works by picking a "pivot" number from an array, positioning every other number in the array in sorted order with respect to the pivot (all smaller numbers to the pivot's left; 
all bigger numbers to the pivot's right), and then repeating the same two steps on both sides of the pivot until the entire array is sorted.

Pick a random number from the input array (the first number, for instance) and let that number be the pivot. 
Iterate through the rest of the array using two pointers, one starting at the left extremity of the array and progressively moving to the right, 
and the other one starting at the right extremity of the array and progressively moving to the left. 
As you iterate through the array, compare the left and right pointer numbers to the pivot. 
    If the left number is greater than the pivot and the right number is less than the pivot, swap them; this will effectively sort these numbers with respect to the pivot at the end of the iteration. 
    If the left number is ever less than or equal to the pivot, increment the left pointer; 
    similarly, if the right number is ever greater than or equal to the pivot, decrement the right pointer. 
Do this until the pointers pass each other, at which point swapping the pivot with the right number should position the pivot in its final,
 sorted position, where every number to its left is smaller and every number to its right is greater.

Repeat the process mentioned on the respective subarrays located to the left and right of your pivot, and keep on repeating the process thereafter until the input array is fully sorted.
"""


def quickSort(array):
    quick_sort_helper(array, 0, len(array)-1)
    return array


def quick_sort_helper(array, start, end):
    if start >= end:
        return

    pivot = start
    # # position every number in the array in sorted order with respect to the array[pivot]
    #   left and right to stop at a place where: left >= pivot & right <= pivot
    left = start + 1
    right = end
    while left <= right:
        # # check if can swap
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]

        # # cannot swap
        elif array[left] <= array[pivot]:  # no need to be swapped
            left += 1
        else:  # if array[right] >= array[pivot]:  # no need to be swapped
            right -= 1

    # # place pivot at correct position (right)
    # we know that once the sorting is done, the number at left >= pivot & right <= pivot
    #   smaller values go to the left of array[pivot]
    array[pivot], array[right] = array[right], array[pivot]

    # # sort to the left & right of array[pivot]
    if (right-1 - start) < (end - right+1):
        quick_sort_helper(array, start, right-1)
        quick_sort_helper(array, right+1, end)
    else:
        quick_sort_helper(array, right+1, end)
        quick_sort_helper(array, start, right-1)
