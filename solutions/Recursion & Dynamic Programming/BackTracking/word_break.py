""" 
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.
Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false

https://leetcode.com/problems/word-break/solution
https://youtu.be/th4OnoGasMU

"""


"""
------------------------- Problem ---------------------------------
string s
dictionary of strings wordDict
return true if s can be segmented into a space-separated sequence of one or more dictionary words.


------------------------- Examples ---------------------------------
s = "applepenapple", wordDict = ["apple","pen"]
True "apple pen apple"

"bacbacbac" ["bacbac"]
False

"appleappapple" ["apple","app"]
True "apple app apple"

s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
False "cats and og"

------------------------- Brute force ---------------------------------
Backtracking O(2^n)
idx = 0
find a word that starts with the char at idx:
    - in None return False
    - if we found one, try complete it (for all of them). If we can complete it, we move idx to the next index after the index at the end of the word
repeat the above steps till the end of the end of the string and return True
    
------------------------- Optimal ---------------------------------

********* Look like a simple Trie problem but it's not ********* 

O(n^3) worst | O(n^2) average
use the memoized brute force

optimal substrcuture: small solutions add up to full

"""


class Solution:
    def wordBreak(self, s: str, wordDict):
        cache = [None] * len(s)
        return self.wordBreakHelper(s, wordDict, 0, cache)

    def wordBreakHelper(self, s, wordDict, idx, cache):
        if idx == len(s):
            return True
        if cache[idx] is not None:
            return cache[idx]

        for word in wordDict:
            if s[idx:idx+len(word)] == word:  # if the word can be completed
                if self.wordBreakHelper(s, wordDict, idx+len(word), cache):
                    cache[idx] = True
                    return cache[idx]

        cache[idx] = False
        return cache[idx]
