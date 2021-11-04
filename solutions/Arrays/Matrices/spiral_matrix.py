"""
Spiral Matrix:

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

https://leetcode.com/problems/spiral-matrix/
"""


# O(n) time | 0(n) space
def spiralTraverse1(array):
    result = []

    rowBegin = columnBegin = 0
    rowEnd = len(array) - 1
    columnEnd = len(array[0]) - 1

    isTop = True
    isRight = isLeft = isBottom = False

    while (rowBegin <= rowEnd and (isBottom or isTop)) or \
            (columnBegin <= columnEnd and (isRight or isLeft)):
        # the `and (isRight or isLeft)` helps prevent addition of an extra element after the traversal is complete
        # print(result)
        if isTop:
            for col in range(columnBegin, columnEnd + 1):
                result.append(array[rowBegin][col])
            rowBegin += 1
            isTop = False
            isRight = True
        elif isRight:
            for row in range(rowBegin, rowEnd+1):
                result.append(array[row][columnEnd])
            columnEnd -= 1
            isBottom = True
            isRight = False
        elif isBottom:
            for col in reversed(range(columnBegin, columnEnd+1)):
                result.append(array[rowEnd][col])
            rowEnd -= 1
            isLeft = True
            isBottom = False
        elif isLeft:
            for row in reversed(range(rowBegin, rowEnd + 1)):
                result.append(array[row][columnBegin])
            columnBegin += 1
            isTop = True
            isLeft = False
    return result


def spiralTraverse(array):
    output = []

    left = 0
    right = len(array[0]) - 1
    top = 0
    bottom = len(array) - 1
    while left <= right or top <= bottom:

        # top
        if top <= bottom:
            for idx in range(left, right+1):
                output.append(array[top][idx])
            top += 1

        # right
        if left <= right:
            for idx in range(top, bottom+1):
                output.append(array[idx][right])
            right -= 1

        # bottom
        if top <= bottom:
            for idx in reversed(range(left, right+1)):
                output.append(array[bottom][idx])
            bottom -= 1

        # left
        if left <= right:
            for idx in reversed(range(top, bottom+1)):
                output.append(array[idx][left])
            left += 1

    return output


# O(n) time | 0(n) space
def spiralTraverse0(array):
    result = []

    top = left = 0
    bottom = len(array) - 1
    right = len(array[0]) - 1

    while (top <= bottom) and (left <= right):

        # top
        for col in range(left, right + 1):
            result.append(array[top][col])

        # right
        for row in range(top + 1, bottom+1):
            result.append(array[row][right])

        # bottom
        for col in reversed(range(left, right)):
            # Handle the edge case when there's a single row
            # in the middle of the matrix. In this case, we don't
            # want to double-count the values in this row, which
            # we've already counted in the first for loop above.
            if top == bottom:
                break
            result.append(array[bottom][col])

        # left
        for row in reversed(range(top + 1, bottom)):
            # Handle the edge case when there's a single column
            # in the middle of the matrix. In this case, we don't
            # want to double-count the values in this column, which
            # we've already counted in the second for loop above.
            if left == right:
                break
            result.append(array[row][left])

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    return result


x = [
    [1, 2, 4],
    [5, 6, 7],
    [8, 9, 10]
]
y = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]
p = [
    [27, 12, 35, 26],
    [25, 21, 94, 11],
    [19, 96, 43, 56],
    [55, 36, 10, 18],
    [96, 83, 31, 94],
    [93, 11, 90, 16]
]
q = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]

print(spiralTraverse1(x))
print(spiralTraverse(x))
print(spiralTraverse1(y))
print(spiralTraverse(y))
print(spiralTraverse1(p))
print(spiralTraverse(p))
print(spiralTraverse1(q))
print(spiralTraverse(q))


"""
Example 1:
    Input:
        [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
        ]
    Output: 
        [1,2,3,6,9,8,7,4,5]

Example 2:
    Input:
        [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
        ]
    Output: 
        [1,2,3,4,8,12,11,10,9,5,6,7]
"""
