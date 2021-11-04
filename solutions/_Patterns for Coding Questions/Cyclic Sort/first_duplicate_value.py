"""
First Duplicate Value:

Given an array of integers between 1 and n, inclusive, where n is the length of the array,
 write a function that returns the first integer that appears more than once (when the array is read from left to right).
In other words, out of all the integers that might occur more than once in the input array,
 your function should return the one whose first duplicate value has the minimum index.
If no integer appears more than once, your function should return -1.
Note that you're allowed to mutate the input array.

https://www.algoexpert.io/questions/First%20Duplicate%20Value
"""


# 0(n) time | 0(n) space
def firstDuplicateValue1(array):
    store = {}
    for num in array:
        if num in store:
            return num
        store[num] = True
    return -1


"""
integers between 1 and n, inclusive, where n is the length of the array
therefore, the array should look like this if sorted [1,2,3,4,5,.....n] if there are no duplicates

- for each number, we can therefore mark it's corresponding index as visited
    - and if we visit an index more than once, then it's repeated

"""


# 0(n) time | 0(1) space
def firstDuplicateValue(array):

    for num in array:
        val = abs(num)
        index = val - 1
        if array[index] < 0:  # if marked
            return val
        array[index] = -array[index]  # mark
    return -1
