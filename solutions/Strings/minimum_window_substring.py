""" 
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

https://leetcode.com/problems/minimum-window-substring

Prerequisites:
- https://leetcode.com/problems/find-all-anagrams-in-a-string/ (https://www.notion.so/paulonteri/Sliding-Window-f6685a15f97a4ca2bb40111e2b264fb2#618e5fb94ea54bee8ff5eb7ab0c155ab)
- https://leetcode.com/problems/permutation-in-string
"""


import collections

""" BF """


class Solution_:

    def minWindow(self, s: str, t: str):
        t_count = collections.Counter(t)
        store = collections.defaultdict(int)

        idx = 0
        while idx < len(s) and not self.hasAllInT(store, t_count):
            store[s[idx]] += 1
            idx += 1

        if not self.hasAllInT(store, t_count):
            return ""

        res = [0, idx-1]
        left = 0
        right = idx-1
        while left <= right and right < len(s):
            # # we have all needed characters
            if left <= right and self.hasAllInT(store, t_count):
                # record size
                res = min(res, [left, right], key=lambda x: x[1]-x[0])

                # reduce size
                store[s[left]] -= 1
                if store[s[left]] == 0:
                    store.pop(s[left])
                left += 1

            # # do not have all needed characters - expand window
            else:
                right += 1
                if right < len(s):
                    store[s[right]] += 1

        return s[res[0]:res[1]+1]

    def hasAllInT(self, store, t_count):

        for char in t_count:
            if char not in store:
                return False
            if store[char] < t_count[char]:
                return False
        return True


""" Optimal """


class Solution:

    def minWindow(self, s: str, t: str):
        t_count = collections.Counter(t)
        window_val_count = collections.defaultdict(int)  # default 0

        res = (0, float("inf"))
        left, right = 0, 0
        # add index 0
        num_of_valid_chars = self.increase_window(
            -1, s, t_count, window_val_count, 0)
        while left <= right and right < len(s):

            # we have all characters - decrease window
            if num_of_valid_chars == len(t_count):
                res = min(res, (left, right), key=lambda x: x[1]-x[0])
                num_of_valid_chars = self.decrease_window(
                    left, s, t_count, window_val_count, num_of_valid_chars)
                left += 1

            # do not have all characters - increase window
            else:
                num_of_valid_chars = self.increase_window(
                    right, s, t_count, window_val_count, num_of_valid_chars)
                right += 1

        if res[1] == float('inf'):
            return ""
        return s[res[0]:res[1]+1]

    def decrease_window(self, left, s, t_count, window_val_count, num_of_valid_chars):
        left_char = s[left]
        if left_char not in t_count:
            return num_of_valid_chars

        had_needed = window_val_count[left_char] >= t_count[left_char]

        window_val_count[left_char] -= 1

        # correct valid chars: one is now missing
        if had_needed and window_val_count[left_char] < t_count[left_char]:
            return num_of_valid_chars-1

        return num_of_valid_chars

    def increase_window(self, right, s, t_count, window_val_count, num_of_valid_chars):
        if right+1 >= len(s):
            return num_of_valid_chars

        right_char = s[right+1]
        if right_char not in t_count:
            return num_of_valid_chars

        had_needed = window_val_count[right_char] >= t_count[right_char]

        window_val_count[right_char] += 1

        # correct valid chars: one is now added
        if not had_needed and window_val_count[right_char] >= t_count[right_char]:
            return num_of_valid_chars+1

        return num_of_valid_chars
