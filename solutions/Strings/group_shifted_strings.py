""" 
249. Group Shifted Strings

We can shift a string by shifting each of its letters to its successive letter.
For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.
For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

Example 1:
    Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
    Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:
    Input: strings = ["a"]
    Output: [["a"]]

https://leetcode.com/problems/group-shifted-strings
"""


import collections


class Solution:
    def getMovement(self, string):
        movement = []
        for i in range(1, len(string)):
            move = ord(string[i]) - ord(string[i-1])
            if move < 0:  # alphabet is a closed loop
                move += 26
            movement.append(move)
        return tuple(movement)

    def groupStrings(self, strings):
        moves = collections.defaultdict(list)

        for string in strings:
            moves[self.getMovement(string)].append(string)

        return list(moves.values())
