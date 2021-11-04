"""
Validate Subsequence:

Given two non-empty arrays of integers,
 write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array.
For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4].
Note that a single number in an array and the array itself are both valid subsequences of the array.

https://www.algoexpert.io/questions/Validate%20Subsequence
"""


# O(n) time | O(1) space - where n is the length of the array
def isValidSubsequence(array, sequence):

    idx = 0
    for num in array:
        # if the num == the value pointer at the sequence, move the pointer at the sequence forward
        if num == sequence[idx]:
            idx += 1

        # return true once the pointer at the sequence == len(sequence)
        if idx == len(sequence):
            return True

    # we did not reach -> (pointer at the sequence == len(sequence))
    return False


"""
Sample Input
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
Sample Output
    true

## SOLUTION:

1. Have two pointers, one at the beginning of each.
2. Iterate throught the array (longer) and:
    - if the value of the pointer at the array == the value pointer at the sequence,
        move the pointer at the sequence forward
    - return true once the pointer at the sequence == len(sequence)
3. return false: we did not reach -> (pointer at the sequence == len(sequence))

"""
