"""
Remove Islands:

You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only 0s and 1s.
The matrix represents a two-toned image, where each 1 represents black and each 0 represents white. An island is defined as any number of 1s that are horizontally or vertically adjacent (but not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent 1s isn't an island if any of those 1s are in the first row, last row, first column, or last column of the input matrix.
Note that an island can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.
You can think of islands as patches of black that don't touch the border of the two-toned image.
Write a function that returns a modified version of the input matrix, where all of the islands are removed. You remove an island by replacing it with 0s.
Naturally, you're allowed to mutate the input matrix.

https://www.algoexpert.io/questions/Remove%20Islands
"""


# O(wh) time | O(wh) space - where w and h
# are the width and height of the input matrix
def removeIslands(matrix):

    for row in range(1, len(matrix)-1):
        for col in range(1, len(matrix[0])-1):

            if matrix[row][col] == 1 and isIsland(matrix, row, col):
                removeOneIsland(matrix, row, col)

    return matrix


def isIsland(matrix, row, col):

    # check if not island
    if matrix[row][col] != 1 or \
        row <= 0 or col <= 0 or \
            row >= len(matrix)-1 or col >= len(matrix[0])-1:
        return False

    matrix[row][col] = -1  # mark

    # check if still island

    up = True
    if row - 1 >= 0 and matrix[row-1][col] == 1:
        up = isIsland(matrix, row-1, col)
    down = True
    if row + 1 < len(matrix) and matrix[row+1][col] == 1:
        down = isIsland(matrix, row+1, col)

    left = True
    if col - 1 >= 0 and matrix[row][col-1] == 1:
        left = isIsland(matrix, row, col-1)
    right = True
    if col + 1 < len(matrix[0]) and matrix[row][col+1] == 1:
        right = isIsland(matrix, row, col+1)

    matrix[row][col] = 1  # unmark

    return left and right and down and up


def removeOneIsland(matrix, row, col):

    if matrix[row][col] == 1:

        matrix[row][col] = 0  # remove

        # down
        if matrix[row+1][col] == 1:
            removeOneIsland(matrix, row+1, col)
        # left
        if matrix[row][col-1] == 1:
            removeOneIsland(matrix, row, col-1)
        # right
        if matrix[row][col+1] == 1:
            removeOneIsland(matrix, row, col+1)


# Solution:
# 1. iterate through every element in the matrix
# 2. chsck if valid island
# 3. if valid island, remove the island


def checkIfIsland(matrix, row, col):
    is_at_end = row <= 0 or col <= 0 or \
        row >= len(matrix)-1 or col >= len(matrix[0])-1

    if is_at_end or matrix[row][col] != 1:
        return False

    matrix[row][col] = -1  # mark

    right = left = up = down = True
    # checks to ensure we don't run into a loop
    if matrix[row][col+1] == 1:  # right
        right = checkIfIsland(matrix, row, col+1)
    if matrix[row][col-1] == 1:  # left
        left = checkIfIsland(matrix, row, col-1)
    if matrix[row+1][col] == 1:  # up
        up = checkIfIsland(matrix, row+1, col)
    if matrix[row-1][col] == 1:  # down
        down = checkIfIsland(matrix, row-1, col)

    matrix[row][col] = 1  # unmark

    return left and right and up and down


def removeAnIsland(matrix, row, col):

    if matrix[row][col] == 1:

        matrix[row][col] = 0  # remove

        # checks to ensure we don't run into a loop
        # down
        if matrix[row+1][col] == 1:
            removeAnIsland(matrix, row+1, col)
        # left
        if matrix[row][col-1] == 1:
            removeAnIsland(matrix, row, col-1)
        # right
        if matrix[row][col+1] == 1:
            removeAnIsland(matrix, row, col+1)


def removeIslands2(matrix):

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if checkIfIsland(matrix, row, col):
                removeAnIsland(matrix, row, col)

    return matrix


"""

Sample Input
    matrix =
    [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
    ]
Sample Output
    [
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1]
    ]
    // The islands that were removed can be clearly seen here:
    // [
    //   [ ,  ,  ,  ,  , ],
    //   [ , 1,  ,  ,  , ],
    //   [ ,  , 1,  ,  , ],
    //   [ ,  ,  ,  ,  , ],
    //   [ ,  , 1, 1,  , ],
    //   [ ,  ,  ,  ,  , ]
    // ]
    
matrix = [[1, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 1, 1],
          [0, 0, 0, 0, 1, 0],
          [1, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 1]
          ]

matrix_2 = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

"""

mx = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

print(removeIslands(mx))
