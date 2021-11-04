"""
Sudoku Solver:

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.



Example 1:

    Input:
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",
        ".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8",
        "5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

https://leetcode.com/problems/sudoku-solver/
https://www.algoexpert.io/questions/Solve%20Sudoku
"""


def solveSudoku(board):
    solveSudokuHelper(board, 0, 0)
    return board


def get_valid_nums(board, row, col):

    def get_all_in_3_by_three(board, row, col, invalid):
        end_row = end_col = 8
        if row <= 2:
            end_row = 2
        elif row <= 5:
            end_row = 5
        if col <= 2:
            end_col = 2
        elif col <= 5:
            end_col = 5

        for i in range(end_row-2, end_row+1):
            for j in range(end_col-2, end_col+1):
                num = board[i][j]
                if num != 0:
                    invalid.add(num)

    def get_all_in_row_and_col(board, row, col, invalid):
        for num in board[row]:
            if num != 0:
                invalid.add(num)
        for i in range(9):
            num = board[i][col]
            if num != 0:
                invalid.add(num)

    invalid = set()
    get_all_in_3_by_three(board, row, col, invalid)
    get_all_in_row_and_col(board, row, col, invalid)

    valid = []
    for num in range(1, 10):
        if num not in invalid:
            valid.append(num)
    return valid


def solveSudokuHelper(board, row, col):
    if row == 9:  # Done
        return True

    # # calculate next
    next_row = row
    next_col = col + 1
    if col == 8:
        next_col = 0
        next_row += 1

    # # fill board
    # check if prefilled
    if board[row][col] != 0:
        return solveSudokuHelper(board, next_row, next_col)

    # trial and error (backtracking)
    for num in get_valid_nums(board, row, col):
        board[row][col] = num  # try with num
        # if we have correctly filled the table, there is no need to try out other nums
        if solveSudokuHelper(board, next_row, next_col):
            return True
        # backtrack: if the input was invalid (the else is not needed but it helps in understanding what is happening)
        else:
            board[row][col] = 0


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


print(solveSudoku(board))
