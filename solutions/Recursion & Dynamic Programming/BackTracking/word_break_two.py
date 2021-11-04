""" 
Word Break II

Given a string s and a dictionary of strings wordDict, 
    add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    Output: ["cats and dog","cat sand dog"]
Example 2:
    Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
    Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
    Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: []

https://leetcode.com/problems/word-break-ii
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]):
        """ 
        - try out all possible words at each index
            - cache the remaining substrings results 

        - backtrack()
            - base cases
            - res []
            - for each word check if it can start at the current index and end successfully
                - if so, call backtrack again 
                    - if it has results, merge the results of that with the current word
                    - add the merged to res
        """

        cache = {}

        def backtrack(idx):
            if idx == len(s):
                return [[]]
            if idx in cache:
                return cache[idx]

            res = []
            for word in wordDict:
                # check if word can start at the current index and end successfully
                if not s[idx:idx+len(word)] == word:
                    continue

                backtrack_res = backtrack(idx+len(word))
                if not backtrack_res:
                    continue

                # merge the results with the current word
                for sentence in backtrack_res:
                    res.append([word]+sentence)

            cache[idx] = res
            return cache[idx]

        return [" ".join(sentence) for sentence in backtrack(0)]
