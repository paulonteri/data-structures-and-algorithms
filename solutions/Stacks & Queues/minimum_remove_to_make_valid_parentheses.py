""" 
Minimum Remove to Make Valid Parentheses:

Given a string s of '(' , ')' and lowercase English characters. 
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
    

Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"
Example 3:
    Input: s = "))(("
    Output: ""
    Explanation: An empty string is also valid.
Example 4:
    Input: s = "(a(b(c)d)"
    Output: "a(b(c)d)"

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses
"""


#

"""
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------- PROBLEM --------------------
- string will have  '(' , ')' and lowercase English characters

- remove the minimum number of parentheses so that the resulting parentheses string is valid
- return any valid string.


------------- EXAMPLES --------------------

a(pp)l)e -> a(pp)le / a(ppl)e -> remove one closing  
a(ppl)e  -> a(ppl)e           -> N/A
a(pple   -> apple             -> remove one opening
a(p(ple  -> apple             -> remove two opening



a(pp()l)e     -> a(pp()l)e                                    -> N/A
lee(t(c)o)de) -> lee(t(c)o)de / lee(t(c)ode)  / lee(t(co)de)  -> remove one closing
a)b(c)d       -> ab(c)d                                       -> remove first closing


a(pp()le 
a(pp()l(e 


"))(("


------------- BRUTE FORCE -------------------- O(n^2) time | O(n) space - where n = len(string)
- count opening and closing then remove the larger randomly and see what works (validate)

------------- OPTIMAL --------------------
------------- 1: O(n) time | O(n) space - where n = len(string)
Two Pass String Builder
- remove any closing bracket that does not have a preceding opening bracket
- remove any excess opening brackets starting at the end


------------- PSEUDOCODE --------------------
------------- 1:
opening_running_count
    (how many unclosed opening brackets we have)

- whenever we meet an opening bracket: opening_running_count += 1
- whenever we meet a closing bracket:
    - if opening_running_count > 0: 
        opening_running_count -= 1
    - else:
        remove it
- remove excess opening brackets starting at the end


"""


class Solution:
    def minRemoveToMakeValid(self, s: str):
        opening_count = 0

        removed_closing = []
        for char in s:
            if char == "(":
                opening_count += 1
                removed_closing.append(char)
            elif char == ")":
                # only add valid ones
                if opening_count > 0:
                    removed_closing.append(char)
                    opening_count -= 1
            else:
                removed_closing.append(char)

        # remove excess opening brackets
        output = [""] * (len(removed_closing) - opening_count)

        curr_idx = len(output) - 1
        for idx in reversed(range(len(removed_closing))):
            # remove
            if removed_closing[idx] == "(" and opening_count > 0:
                opening_count -= 1
            else:
                output[curr_idx] = removed_closing[idx]
                curr_idx -= 1

        return "".join(output)


class _Solution:
    def removeInvalidClosingbrackets(self, s, opening, closing):
        result = []

        opening_count = 0
        for char in s:
            if char == opening:
                opening_count += 1
                result.append(char)
            elif char == closing:
                # only add valid ones
                if opening_count > 0:
                    result.append(char)
                    opening_count -= 1
            else:
                result.append(char)

        return result

    def minRemoveToMakeValid(self, s: str):

        # remove excess brackets
        removed_closing = self.removeInvalidClosingbrackets(s, "(", ")")
        removed_opening = reversed(self.removeInvalidClosingbrackets(reversed(removed_closing),
                                                                     ")", "("))
        return "".join(removed_opening)


""" 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
If we put the indexes of the "(" on the stack, then we'll know that all the indexes on the stack at the end are the indexes of the unmatched "(". 
We should also use a set to keep track of the unmatched ")" we come across.
"""


class Solution1:
    def minRemoveToMakeValid(self, s: str):
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            # opening brackets
            if c == "(":
                stack.append(i)

            # closing brackets
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()

        # the union of two sets contains all the elements contained in either set (or both sets).
        indexes_to_remove = indexes_to_remove.union(set(stack))

        # build string with skipping invalid parenthesis
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)
