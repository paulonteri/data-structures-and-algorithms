"""
Sort Characters By Frequency: Leetcode 451

Given a string, sort it in decreasing order based on the frequency of characters.

https://leetcode.com/problems/sort-characters-by-frequency/
"""


from collections import defaultdict


class Solution:
    def frequencySort(self, s: str):

        if not s:
            return ""

        store = {}

        # count occurrences of each character
        for char in s:
            if char in store:
                store[char] = 1 + store[char]
            else:
                store[char] = 1

        # store dictionary keys sorted by the number of occurrences
        sorted_chars_list = sorted(store, key=lambda x: store[x], reverse=True)

        # rebuild string
        str_temp = []
        for char in sorted_chars_list:
            str_temp.append(char * store[char])

        return "".join(str_temp)


"""
Input:
    "tree"
    "cccaaa"
    "Aabb"
    ""
Output:
    "eetr"
    "cccaaa"
    "bbAa"
    ""
"""


class Solution00:
    def frequencySort(self, s: str):
        char_store = defaultdict(int)

        # count char frequency
        for char in s:
            char_store[char] += 1

        # list of characters sorted by their frequency
        sorted_char_list = sorted(
            char_store,
            key=lambda x: char_store[x],
            reverse=True
        )

        # rebuild string with correct character frequency
        res = []
        for char in sorted_char_list:
            res.append(char*char_store[char])
        return "".join(res)
