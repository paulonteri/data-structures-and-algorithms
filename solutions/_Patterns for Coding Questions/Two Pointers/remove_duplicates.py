""" 
Remove Duplicates;

Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

"""

""" 
Solution 1;

- have a res_length variable that will be initialised as 1
- have two pointers both at the start of the array: left & right
- move the right pointer one step forward:
    - if its value is not equal to left's value, increment the value of res_length & move the left pointer to right's position
    - if equal, repeat this step (move the right pointer one step forward)

[2, 3, 3, 3, 6, 9, 9]
l=2,r=2,res=1
l=3,r=3,res=2
l=3,r=3,res=2
l=3,r=3,res=2
l=6,r=6,res=3
l=9,r=9,res=4
l=9,r=9,res=4
"""


def remove_duplicates(arr):

    res_length = 1
    last_non_dup = 0
    for idx in range(1, len(arr)):
        if arr[last_non_dup] != arr[idx]:
            res_length += 1
            last_non_dup = idx
    return res_length


""" 
Solution 2:

In this problem, we need to remove the duplicates in-place such that the resultant length of the array remains sorted. 
As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we encounter duplicates. 
In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number. 
So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.
"""


def remove_duplicates2(arr):
    next_non_duplicate = 1

    for i in range(1, len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate
