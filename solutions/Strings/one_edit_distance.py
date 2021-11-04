""" 
161. One Edit Distance

Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
A string s is said to be one distance apart from a string t if you can:
    Insert exactly one character into s to get t.
    Delete exactly one character from s to get t.
    Replace exactly one character of s with a different character to get t.
 
Example 1:
    Input: s = "ab", t = "acb"
    Output: true
    Explanation: We can insert 'c' into s to get t.
Example 2:
    Input: s = "", t = ""
    Output: false
    Explanation: We cannot get t from s by only one step.
Example 3:
    Input: s = "a", t = ""
    Output: true
Example 4:
    Input: s = "", t = "A"
    Output: true    

https://leetcode.com/problems/one-edit-distance

do https://leetcode.com/problems/edit-distance after this
"""


class Solution:

    def isOneEditDistance(self, s: str, t: str):
        # ensure one edit distance
        if abs(len(t) - len(s)) > 1:
            return False
        if s == t:
            return False
        # ensure t is longer
        if len(t) < len(s):
            return self.isOneEditDistance(t, s)

        edited = False
        s_idx, t_idx = 0, 0
        while s_idx < len(s) or t_idx < len(t):
            # one of them has reached end
            if s_idx == len(s) or t_idx == len(t):
                if edited or t_idx == len(t):
                    return False
                # can remove last element
                return t_idx == len(t)-1

            # same char
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1

            # try delete from t
            elif self.is_valid_move(s, t, s_idx, t_idx+1) and not edited:
                t_idx += 1
                edited = True

            # try replace
            elif self.is_valid_move(s, t, s_idx+1, t_idx+1) and not edited:
                s_idx += 1
                t_idx += 1
                edited = True
            # try insert
            # if we know len(t) is always longer or equal to len(s),
            #   replaces and deletes will work
            #   insert does the opposite of delete
            else:
                return False

        return edited

    def is_valid_move(self, s, t, s_idx, t_idx):
        if s_idx == len(s) or t_idx == len(t):
            return s_idx == len(s) and t_idx == len(t)

        if s[s_idx] == t[t_idx]:
            return True

        return False
