""" 
Sorted Squared Array:

Write a function that takes in a non-empty array of integers that are sorted in ascending order
 and returns a new array of the same length with 
 the squares of the original integers also sorted in ascending order.

Sample Input
    array = [1, 2, 3, 5, 6, 8, 9]
Sample Output
    [1, 4, 9, 25, 36, 64, 81]

https://www.algoexpert.io/questions/Sorted%20Squared%20Array
"""


def sortedSquaredArray(array):
    output = [0] * len(array)

    start = 0
    end = len(array) - 1

    pos = len(array) - 1
    while start <= end:
        if abs(array[end]) >= abs(array[start]):
            output[pos] = array[end]**2
            end -= 1
        else:
            output[pos] = array[start]**2
            start += 1

        pos -= 1

    return output


"""
have two pointers one at each end, 
then fill the result array with the (larger abs value)**2

[-9, -5, -2, -1, 1, 4, 9, 25, 36, 64, 81]

[1, 1, -2, 4, -5, -9, 9, 25, 36, 64, 81 ] -> this should be squared
"""
