""" 
Minimum Passes Of Matrix:

Write a function that takes in an integer matrix of potentially unequal height and width and 
    returns the minimum number of passes required to convert all negative integers in the matrix to positive integers.
A negative integer in the matrix can only be converted to a positive integer if one or more of its adjacent elements is positive. 
An adjacent element is an element that is to the left, to the right, above, or below the current element in the matrix. 
Converting a negative to a positive simply involves multiplying it by -1.
Note that the 0 value is neither positive nor negative, meaning that a 0 can't convert an adjacent negative to a positive.
A single pass through the matrix involves converting all the negative integers that can be converted at a particular point in time. 
For example, consider the following input matrix:
    [ 
    [0, -2, -1], 
    [-5, 2, 0], 
    [-6, -2, 0],
    ]

    After a first pass, only 3 values can be converted to positives:

    [ 
    [0, 2, -1], 
    [5, 2, 0], 
    [-6, 2, 0],
    ]

    After a second pass, the remaining negative values can all be converted to positives:

    [ 
    [0, 2, 1], 
    [5, 2, 0], 
    [6, 2, 0],
    ]

Note that the input matrix will always contain at least one element. If the negative integers in the input matrix can't all be converted to positives, regardless of how many passes are run, your function should return -1.

Sample Input
    matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1],
    ]
Sample Output
    3

https://www.algoexpert.io/questions/Minimum%20Passes%20Of%20Matrix
"""


""" 
- res = 0
- add all positive numbers to a queue
- for each number in the queue:
    - remove it from the queue
    - convert all positive neighbours to positive and add them to the next queue
    - if a number was converted, increment res by one
    - repeat these steps until the queue is empty
"""


def minimumPassesOfMatrix(matrix):
    number = removeNegatives(matrix)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # negative not removed
            if matrix[row][col] < 0:
                return -1

    return number


def removeNegatives(matrix):
    res = 0
    queue = []

    # create initial queue
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                queue.append((row, col))

    # remove negatives
    while queue:
        has_negative = False
        for _ in range(len(queue)):
            row, col = queue.pop(0)

            # left
            if col-1 >= 0 and matrix[row][col-1] < 0:
                has_negative = True
                matrix[row][col-1] = matrix[row][col-1] * -1
                queue.append((row, col-1))

            # right
            if col+1 < len(matrix[0]) and matrix[row][col+1] < 0:
                has_negative = True
                matrix[row][col+1] = matrix[row][col+1] * -1
                queue.append((row, col+1))

            # above
            if row-1 >= 0 and matrix[row-1][col] < 0:
                has_negative = True
                matrix[row-1][col] = matrix[row-1][col] * -1
                queue.append((row-1, col))

            # below
            if row+1 < len(matrix) and matrix[row+1][col] < 0:
                has_negative = True
                matrix[row+1][col] = matrix[row+1][col] * -1
                queue.append((row+1, col))

        if has_negative:
            res += 1

    return res
