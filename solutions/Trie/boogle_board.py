""" 
Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, 
    where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
https://leetcode.com/problems/word-search-ii/
"""

"""
Boggle Board:
You're given a two-dimensional array (a matrix) of potentially unequal height and width containing letters;
 this matrix represents a boggle board. You're also given a list of words.
Write a function that returns an array of all the words contained in the boggle board. The final words don't need to be in any particular order.
A word is constructed in the boggle board by connecting adjacent (horizontally, vertically, or diagonally) letters,
 without using any single letter at a given position more than once; while a word can of course have repeated letters,
 those repeated letters must come from different positions in the boggle board in order for the word to be contained in the board.
Note that two or more words are allowed to overlap and use the same letters in the boggle board.

Sample Input
    board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"],
    ],
    words = [
    "this", "is", "not", "a", "simple", "boggle",
    "board", "test", "REPEATED", "NOTRE-PEATED",
    ]
Sample Output
    ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
    // The words could be ordered differently.

https://www.algoexpert.io/questions/Boggle%20Board
"""


""" 
------------------------------------------------------------------------------------------------------------------------------
"""


def boggleBoardBF(board, words):
    found_words = []

    for row in range(len(board)):
        for col in range(len(board[row])):

            # look for each word
            for idx in range(len(words)):
                if words[idx] != '-1':
                    if find_word(board, words, found_words, idx, 0, row, col):
                        found_words.append(words[idx])
                        # mark word as visted
                        words[idx] = '-1'

    return found_words


def find_word(board, words, found_words, curr_word_idx,  curr_char_idx, row, col):
    # had found word
    if words[curr_word_idx] == '-1':
        return False

    word = words[curr_word_idx]

    # found word
    if curr_char_idx >= len(word):
        return True

    # out of bounds
    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
        return False

    # was visited
    if board[row][col] == '000':
        return False

    curr_char = board[row][col]

    # cannot make word
    if curr_char != word[curr_char_idx]:
        return False

    # mark as visited
    board[row][col] = '000'

    # explore
    top = find_word(board, words, found_words, curr_word_idx,
                    curr_char_idx+1, row+1, col)
    bottom = find_word(board, words, found_words, curr_word_idx,
                       curr_char_idx+1, row-1, col)
    left = find_word(board, words, found_words, curr_word_idx,
                     curr_char_idx+1, row, col-1)
    right = find_word(board, words, found_words, curr_word_idx,
                      curr_char_idx+1, row, col+1)
    top_left = find_word(board, words, found_words, curr_word_idx,
                         curr_char_idx+1, row+1, col-1)
    top_right = find_word(board, words, found_words, curr_word_idx,
                          curr_char_idx+1, row+1, col+1)
    bottom_left = find_word(board, words, found_words, curr_word_idx,
                            curr_char_idx+1, row-1, col-1)
    bottom_right = find_word(board, words, found_words, curr_word_idx,
                             curr_char_idx+1, row-1, col+1)

    # unmark
    board[row][col] = curr_char

    return top or bottom or left or right or top_left or top_right or bottom_left or bottom_right


""" 
------------------------------------------------------------------------------------------------------------------------------

use a Trie
"""


""" 
------------------------------------------------------------------------------------------------------------------------------

use a Trie
"""

endSymbol = "*"


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = endSymbol

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word

    def remove(self, word):
        self.delete(self.root, word, 0)

    def delete(self, dicts, word, i):
        if i == len(word):
            if '*' in dicts:
                del dicts['*']
                if len(dicts) == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if word[i] in dicts and self.delete(dicts[word[i]], word, i + 1):
                if len(dicts[word[i]]) == 0:
                    del dicts[word[i]]
                    return True
                else:
                    return False

            else:
                return False


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.add(word)

        found_words = {}

        for row in range(len(board)):
            for col in range(len(board[row])):
                self.explore(trie, row, col, trie.root, board, found_words)

        return list(found_words.keys())

    def get_neighbours(self, i, j, board):
        neighbours = []
        if i > 0:
            neighbours.append([i - 1, j])
        if i < len(board) - 1:
            neighbours.append([i + 1, j])
        if j > 0:
            neighbours.append([i, j - 1])
        if j < len(board[0]) - 1:
            neighbours.append([i, j + 1])
        return neighbours

    def explore(self, main_trie, row, col, trie, board, found_words):
        mark = -1

        # # validate
        if board[row][col] not in trie:
            return
        if board[row][col] == mark:
            return

        char = board[row][col]
        curr_trie = trie[char]

        # # record all words found
        if endSymbol in curr_trie:
            word = curr_trie[endSymbol]
            found_words[word] = True
            main_trie.remove(word)

        # # continue search
        board[row][col] = mark  # visit - mark visited
        for neighbour in self.get_neighbours(row, col, board):
            self.explore(
                main_trie, neighbour[0], neighbour[1], curr_trie, board, found_words)
        board[row][col] = char  # univisit - remove mark


""" 
---------------------------------------------------------
"""


def get_neighbours(i, j, board):

    neighbours = []

    if i > 0 and j > 0:
        neighbours.append([i - 1, j - 1])
    if i > 0 and j < len(board[0]) - 1:
        neighbours.append([i - 1, j + 1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbours.append([i + 1, j + 1])
    if i < len(board) - 1 and j > 0:
        neighbours.append([i + 1, j - 1])
    if i > 0:
        neighbours.append([i - 1, j])
    if i < len(board) - 1:
        neighbours.append([i + 1, j])
    if j > 0:
        neighbours.append([i, j - 1])
    if j < len(board[0]) - 1:
        neighbours.append([i, j + 1])
    return neighbours


def explore(row, col, trie, board, found_words):
    mark = -1

    # # validate
    if board[row][col] not in trie:
        return
    if board[row][col] == mark:
        return

    char = board[row][col]
    curr_trie = trie[char]

    # # record all words found
    if "*" in curr_trie:
        found_words[curr_trie["*"]] = True

    # # continue search
    board[row][col] = mark  # visit - mark visited
    for neighbour in get_neighbours(row, col, board):
        explore(neighbour[0], neighbour[1], curr_trie, board, found_words)
    board[row][col] = char  # univisit - remove mark


def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)

    found_words = {}

    for row in range(len(board)):
        for col in range(len(board[row])):
            explore(row, col, trie.root, board, found_words)

    return list(found_words.keys())


""" 
------------------------------------------------------------------------------------------------------------------------------
"""
