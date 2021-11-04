""" 
N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

https://leetcode.com/problems/n-queens/
https://www.algoexpert.io/questions/Non-Attacking%20Queens

"""


""" 
Time complexity:
   row: num of placements * time complexity for validating placement == n
    0 : n      * n
    1 : n-2 (remove column & diagonal of prev)    * n
    2 : n-4    * n
    3 : n-6    * n
    ...

    total => n! * n

"""


class Solution:
    def solveNQueens(self, n):

        result = []
        self.solve_n_queens_helper(n, result, set(), 0)
        return result

    def solve_n_queens_helper(self, n, result, placed, row):
        if row == n:
            self.build_solution(n, placed, result)
            return

        for col in range(n):
            # place
            placed.add((row, col))

            if self.is_valid_placement(n, placed):
                self.solve_n_queens_helper(n, result, placed, row+1)

            # remove
            placed.discard((row, col))

    def is_valid_placement(self, n, placed):

        # check columns
        cols = set()
        for item in placed:
            cols.add(item[1])
        if len(cols) < len(placed):
            return False

        # check positive diagonal
        # explanation: https://www.notion.so/paulonteri/Recursion-DP-Backtracking-525dddcdd0874ed98372518724fc8753#d51d8aa004ff49a4a0bf49c755fdf193
        pos_diagonal = set()
        for item in placed:
            row, col = item
            pos_diagonal.add(row - col)
        if len(pos_diagonal) < len(placed):
            return False

        # check negative diagonal
        neg_diagonal = set()
        for item in placed:
            row, col = item
            neg_diagonal.add(row + col)
        if len(neg_diagonal) < len(placed):
            return False

        return True

    def build_solution(self, n, placed, result):
        # result.append(list(placed))
        board = [["." for _ in range(n)]for _ in range(n)]

        for item in placed:
            row, col = item
            board[row][col] = "Q"

        for idx in range(n):
            board[idx] = "".join(board[idx])

        result.append(board)


""" 

"""


class Solution_:
    def solveNQueens(self, n):

        result = []
        board = [["." for _ in range(n)]for _ in range(n)]
        self.solve_n_queens_helper(
            n, board, result, set(), 0, set(), set(), set())
        return result

    def solve_n_queens_helper(self, n, board, result, placed, row, cols_placed, pos_diagonal, neg_diagonal):
        if row == n:
            # print(board)
            board_copy = board[:]
            for idx in range(n):
                board_copy[idx] = "".join(board_copy[idx])
            result.append(board_copy)
            return

        for col in range(n):
            # place
            added = self.add_placement_info(
                row, col, placed, cols_placed, pos_diagonal, neg_diagonal)

            if added:
                board[row][col] = "Q"
                self.solve_n_queens_helper(
                    n, board, result, placed, row+1, cols_placed, pos_diagonal, neg_diagonal)

                # remove
                self.remove_placement_info(
                    row, col, placed, cols_placed, pos_diagonal, neg_diagonal)
                board[row][col] = "."

    def add_placement_info(self, row, col, placed, cols_placed, pos_diagonal, neg_diagonal):
        # explanation: https://www.notion.so/paulonteri/Recursion-DP-Backtracking-525dddcdd0874ed98372518724fc8753#d51d8aa004ff49a4a0bf49c755fdf193
        if col in cols_placed or row-col in pos_diagonal or row+col in neg_diagonal:
            return False
        placed.add((row, col))
        cols_placed.add(col)
        pos_diagonal.add(row - col)
        neg_diagonal.add(row + col)
        return True

    def remove_placement_info(self, row, col, placed,  cols_placed, pos_diagonal, neg_diagonal):
        # explanation: https://www.notion.so/paulonteri/Recursion-DP-Backtracking-525dddcdd0874ed98372518724fc8753#d51d8aa004ff49a4a0bf49c755fdf193
        placed.discard((row, col))
        cols_placed.discard(col)
        pos_diagonal.discard(row - col)
        neg_diagonal.discard(row + col)
