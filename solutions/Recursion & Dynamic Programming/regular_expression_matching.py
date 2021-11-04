""" 
Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

 

Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:
    Input: s = "aab", p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:
    Input: s = "mississippi", p = "mis*is*p*."
    Output: false

https://leetcode.com/problems/regular-expression-matching/
"""

"""
Basic Regex Parser:

Implement a regular expression function isMatch that supports the '.' and '*' symbols. 
The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. 
For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.
In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, 
    where the '.' is treated as a single a character wildcard (see third example), 
    and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). 
For more information on regular expression matching, see the Regular Expression Wikipedia page.

Explain your algorithm, and analyze its time and space complexities.

Examples:

input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true

https://www.pramp.com/challenge/KvZ3aL35Ezc5K9Eq9Llp
"""


class Solution:
    def isMatch(self, text, pattern):
        if len(text) == 0 and len(pattern) == 0:
            return True
        if len(pattern) == 0:
            return False

        return self.is_match_helper(text, pattern, 0, 0)

    def is_match_helper(self, text, pattern, text_idx, pattern_idx):
        # base cases
        if text_idx == len(text):
            if pattern_idx == len(pattern):
                return True
            if pattern_idx+1 < len(pattern) and pattern[pattern_idx+1] == '*':
                return self.is_match_helper(text, pattern, text_idx, pattern_idx+2)
            return False
        if pattern_idx == len(pattern):
            return False

        # '*'
        if pattern_idx < len(pattern)-1 and pattern[pattern_idx+1] == '*':
            prev_char = pattern[pattern_idx]

            # many of prev_char
            after_pattern = text_idx
            if prev_char == ".":
                after_pattern = len(text)
            else:
                while after_pattern < len(text) and text[after_pattern] == prev_char:
                    after_pattern += 1

            # try all possibilities
            for idx in range(text_idx, after_pattern+1):
                if self.is_match_helper(text, pattern, idx, pattern_idx+2):
                    return True
            return False

        # '.'
        elif pattern[pattern_idx] == '.':
            return self.is_match_helper(text, pattern, text_idx+1, pattern_idx+1)

        # other characters
        else:
            if pattern[pattern_idx] != text[text_idx]:
                return False

            return self.is_match_helper(text, pattern, text_idx+1, pattern_idx+1)


"""
"""


class Solution_:
    def isMatch(self, text, pattern):
        if len(text) == 0 and len(pattern) == 0:
            return True
        if len(pattern) == 0:
            return False

        cache = [[None for _ in range(len(pattern))] for _ in range(len(text))]
        return self.is_match_helper(text, pattern, cache, 0, 0)

    def is_match_helper(self, text, pattern, cache, text_idx, pattern_idx):
        # base cases
        if text_idx == len(text):
            if pattern_idx == len(pattern):
                return True
            if pattern_idx+1 < len(pattern) and pattern[pattern_idx+1] == '*':
                return self.is_match_helper(text, pattern, cache, text_idx, pattern_idx+2)
            return False
        if pattern_idx == len(pattern):
            return False
        if cache[text_idx][pattern_idx] is not None:
            return cache[text_idx][pattern_idx]

        # '*'
        if pattern_idx < len(pattern)-1 and pattern[pattern_idx+1] == '*':
            prev_char = pattern[pattern_idx]

            # many of prev_char
            after_pattern = text_idx
            if prev_char == ".":
                after_pattern = len(text)
            else:
                while after_pattern < len(text) and text[after_pattern] == prev_char:
                    after_pattern += 1

            # try all possibilities
            for idx in range(text_idx, after_pattern+1):
                if self.is_match_helper(text, pattern, cache, idx, pattern_idx+2):
                    cache[text_idx][pattern_idx] = True
                    return cache[text_idx][pattern_idx]

            cache[text_idx][pattern_idx] = False
            return cache[text_idx][pattern_idx]

        # '.'
        elif pattern[pattern_idx] == '.':
            cache[text_idx][pattern_idx] = self.is_match_helper(
                text, pattern, cache, text_idx+1, pattern_idx+1)
            return cache[text_idx][pattern_idx]

        # other characters
        else:
            if pattern[pattern_idx] != text[text_idx]:
                cache[text_idx][pattern_idx] = False
            else:
                cache[text_idx][pattern_idx] = self.is_match_helper(
                    text, pattern, cache, text_idx+1, pattern_idx+1)
            return cache[text_idx][pattern_idx]
