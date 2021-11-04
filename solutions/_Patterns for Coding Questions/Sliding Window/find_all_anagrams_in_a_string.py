""" 
Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
        The substring with start index = 0 is "ab", which is an anagram of "ab".
        The substring with start index = 1 is "ba", which is an anagram of "ab".
        The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:
    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.

https://leetcode.com/problems/find-all-anagrams-in-a-string/
Prerequisite: 
- https://leetcode.com/problems/permutation-in-string
"""
import collections


# Time complexity: O(S) + O(P) since it's one pass along both strings.
# Note: we can compare p_count and window_count in constant time because they are both at most size 26
# Space complexity: O(1) because p_count and window_count contain not more than 26 elements.
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return[]
        anagrams = []

        # an array of length 26 can be used instead (with the ASCII values of the characters)
        p_count = collections.Counter(p)
        window_count = collections.Counter()
        for idx, char in enumerate(s):
            # # create window
            if idx < len(p):
                window_count[char] += 1

            # # move window forward
            else:
                # remove char at left end
                left_end_char = s[idx-(len(p))]
                window_count[left_end_char] -= 1
                if window_count[left_end_char] == 0:
                    window_count.pop(left_end_char)
                # add char to right end
                window_count[char] += 1

            # # check if anagrams
            if p_count == window_count:
                anagrams.append(idx-(len(p)-1))

        return anagrams
