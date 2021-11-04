"""
Magic Index: 

A magic index in an array A[ 0••• n -1] is defined to be an index such that A[ i] = i. 
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

FOLLOW UP:
What if the values are not distinct?

CTI 8.4
"""

""" 
What if the values are not distinct? - cannot use two pointers
"""


def magicIndex(array):
    return magicIndexHelper(array, 0, len(array)-1)


def magicIndexHelper(array, left, right):

    if left > right:
        return -1

    mid = (left+right) // 2
    if array[mid] == mid:
        return mid

    left_side = magicIndexHelper(array, left, min(mid-1, array[mid]))
    right_side = magicIndexHelper(array,  max(mid+1, array[mid]), right)

    if left_side >= 0:
        return left_side
    elif right_side >= 0:
        return right_side

    return -1


def FillArray():
    array = [0] * 10
    array[0] = -14
    array[1] = -12
    array[2] = 0
    array[3] = 1
    array[4] = 2
    array[5] = 5
    array[6] = 9
    array[7] = 10
    array[8] = 23
    array[9] = 25
    return array


array = FillArray()
print(magicIndex(array))
print(magicIndex([1, 3, 2, 4, 5]))
print(magicIndex([0, 6, 6, 6, 6]))
print(magicIndex([1, 4, 4, 4, 4]))
