""" 
Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example 1
    Input: s = "aab"
    Output: "aba"
Example 2:
    Input: s = "aaab"
    Output: ""
3:
    "aaaabbbbbccd"
    "babababcabcd"

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.

https://leetcode.com/problems/reorganize-string
"""

from collections import Counter
from heapq import heapify, heappush, heappop


class Solution:
    def reorganizeString(self, s: str):
        """ 
        The goal is to first exhaust the most-frequent chars. 
            We build a frequency dict of the letters in the string. We push all the letters into a max heap together with their frequencies
        We pop two letters at a time from the heap, add them to our result string, decrement their frequencies and push them back into heap. 
            Why do we have to pop two items/letters at a time you're wondering? 
            Because if we only pop one at a time, we will keep popping and pushing the same letter over and over again if that letter has a freq greater than 1. 
            Hence by popping two at time, adding them to result, decrementing their freq and finally pushing them back into heap, we guarantee that we are always alternating between letters.
        https://leetcode.com/problems/reorganize-string/discuss/492827/Python-Simple-heap-solution-with-detailed-explanation
        """
        res = []

        character_count = [(-count, char)
                           for char, count in Counter(s).items()]
        heapify(character_count)
        while len(res) < len(s):
            # # add most frequent
            # 1
            count_1, char_1 = heappop(character_count)
            count_1 *= -1
            res.append(char_1)
            # 2
            count_2 = 0
            if character_count:
                count_2, char_2 = heappop(character_count)
                count_2 *= -1
                res.append(char_2)

            # # return into heap
            if count_1 > 1:
                count_1 -= 1
                heappush(character_count, (-count_1, char_1))
            if count_2 > 1:
                count_2 -= 1
                heappush(character_count, (-count_2, char_2))

        for idx in range(1, len(s)):
            if res[idx-1] == res[idx]:
                return ""

        return "".join(res)
