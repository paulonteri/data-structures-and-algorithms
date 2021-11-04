""" 
Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

Constraints:
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters

https://leetcode.com/problems/permutation-in-string

Do after this: 
- https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""

from collections import Counter


# Note: we can compare p_count and window_count in constant time because they are both at most size 26
# Space complexity: O(1) because p_count and window_count contain not more than 26 elements.
class Solution:
    def checkInclusion(self, s1: str, s2: str):

        # # create counters
        window_counter = [0] * 26
        s1_counter = [0] * 26
        for char, count in Counter(s1).items():
            s1_counter[self.char_idx(char)] = count

        # # look for permutations using a sliding window pattern
        for idx in range(len(s2)):

            # # create first window
            if idx < (len(s1)):
                window_counter[self.char_idx(s2[idx])] += 1

            # # move window forward
            else:
                window_counter[self.char_idx(s2[idx-len(s1)])] -= 1
                window_counter[self.char_idx(s2[idx])] += 1

            # # check for result
            if s1_counter == window_counter:
                return True

    def char_idx(self, char):
        return ord(char) - ord('a')
