"""
Smallest Difference:

Write a function that takes in two non-empty arrays of integers,
 finds the pair of numbers (one from each array) whose absolute difference is closest to zero,
 and returns an array containing these two numbers, with the number from the first array in the first position.

Note that the absolute difference of two integers is the distance between them on the real number line. 
For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.

https://www.algoexpert.io/questions/Smallest%20Difference
"""


# Start by sorting both arrays.
# Put a pointer at the beginning of both arrays and evaluate the absolute difference of the pointer-numbers.
# If the difference is equal to zero, then you've found the closest pair;
#  otherwise, increment the pointer of the smaller of the two numbers to find a potentially better pair.
# Continue until you get a pair with a difference of zero or until one of the pointers gets out of range of its array.

# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference01(arrayOne, arrayTwo):
    res = [float('inf'), float('-inf')]
    arrayOne.sort()
    arrayTwo.sort()

    one = 0
    two = 0
    while one < len(arrayOne) and two < len(arrayTwo):
        val_one = arrayOne[one]
        val_two = arrayTwo[two]

        if abs(val_one - val_two) < abs(res[0]-res[1]):
            res = [val_one, arrayTwo[two]]

        # # move to next
        if val_one > val_two:
            two += 1
        elif val_two > val_one:
            one += 1
        else:
            return [val_one, val_two]

    return res
