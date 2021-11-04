"""
Word Search

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where "adjacent" cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Constraints:
    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3

https://leetcode.com/problems/word-search/
"""

from typing import List


# O(n) time | O(n) space -> because of the recursion call stack |
class Solution:
    def exist(self, board: List[List[str]], word: str):

        # Iterate over each character
        h = 0
        while h < len(board):
            w = 0
            while w < len(board[0]):
                # stop iteration if we find the word
                if board[h][w] == word[0] and self.searchWordOutward(board, word, h, w, 0):
                    return True
                w += 1
            h += 1

        return False

    def searchWordOutward(self, board, word, h, w, word_pos):
        # check if past end of word (found all characters)
        if word_pos >= len(word):
            return True

        if h < 0 or h >= len(board) or \
                w < 0 or w >= len(board[0]):
            return False

        if board[h][w] != word[word_pos]:
            return False

        # remove seen character
        seen_char = board[h][w]
        board[h][w] = ''

        # Expand: move on to next character (word_pos + 1) -> in the order right, left, top, bottom
        found = self.searchWordOutward(board, word, h, w+1, word_pos+1) or \
            self.searchWordOutward(board, word, h, w-1, word_pos+1) or \
            self.searchWordOutward(board, word, h+1, w, word_pos+1) or \
            self.searchWordOutward(board, word, h-1, w, word_pos+1)

        # return seen character
        board[h][w] = seen_char

        return found


"""
Input:
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    "ABCCED"
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    "SEE"
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    "ABCB"
Output:
    true
    true
    false
"""
