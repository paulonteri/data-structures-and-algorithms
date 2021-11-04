"""
River Sizes:

You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s.
Each 0 represents land, and each 1 represents part of a river.
A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent).
The number of adjacent 1s forming a river determine its size.
Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.
Write a function that returns an array of the sizes of all rivers represented in the input matrix. 
The sizes don't need to be in any particular order.

Sample Input
    matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    ]
Sample Output
    [1, 2, 2, 2, 5] // The numbers could be ordered differently.

// The rivers can be clearly seen here:
// [
//   [1,  ,  , 1,  ],
//   [1,  , 1,  ,  ],
//   [ ,  , 1,  , 1],
//   [1,  , 1,  , 1],
//   [1,  , 1, 1,  ],
// ]

https://www.algoexpert.io/questions/River%20Sizes
"""

"""
Solution:
1. iterate through every element in the array
2. if we find a river (1) map out it's length while marking the river's elements as visited (-1)
"""


# O(wh) time | O(wh) space
def riverSizes(matrix):
    river_sizes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            if matrix[row][col] == 1:  # if river
                river_sizes.append(findRiverSize(matrix, row, col))

    return river_sizes


def findRiverSize(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) \
            or matrix[row][col] != 1:  # not river (base case)
        return 0

    matrix[row][col] = -1  # mark point as visited

    left = findRiverSize(matrix, row, col-1)
    right = findRiverSize(matrix, row, col+1)
    down = findRiverSize(matrix, row+1, col)
    up = findRiverSize(matrix, row-1, col)

    return 1 + right + left + down + up  # visit neighbours


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]
x = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
]  # [2, 1, 21, 5, 2, 1]
print(riverSizes(matrix))
print(riverSizes([[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]))
print(riverSizes(x))
# print(findRiverSize(x, 0, 5))
