"""
301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return all the possible results. You may return the answer in any order.s

Example 1:
    Input: s = "()())()"
    Output: ["(())()","()()()"]
Example 2:
    Input: s = "(a)())()"
    Output: ["(a())()","(a)()()"]
Example 3:
    Input: s = ")("
    Output: [""]

https://leetcode.com/problems/remove-invalid-parentheses
https://youtu.be/cp0H_aR3OZo
"""


class Solution:
    def removeInvalidParentheses(self, s):
        result = set()
        invalid_opening, invalid_closing = self.count_invalid(s)

        self.valid_builder(s, result, [], 0, invalid_opening, invalid_closing)
        return list(result)

    def valid_builder(self, s, result, curr, idx, invalid_opening, invalid_closing):
        if idx == len(s):
            if invalid_opening == 0 and invalid_closing == 0 and self.is_valid(curr):
                result.add("".join(curr))
            return
        char = s[idx]

        # can remove opening
        if char == "(" and invalid_opening > 0:
            self.valid_builder(
                s, result, curr, idx+1, invalid_opening-1, invalid_closing)
        # can remove closing
        if char == ")" and invalid_closing > 0:
            self.valid_builder(
                s, result, curr, idx+1, invalid_opening, invalid_closing-1)

        # add regardless
        self.valid_builder(
            s, result, curr+[char], idx+1, invalid_opening, invalid_closing)

    def count_invalid(self, s):
        invalid_closing = 0
        invalid_opening = 0

        # invalid closing
        opening_remaining = 0
        for char in s:
            if char == "(":
                opening_remaining += 1
            elif char == ")":
                if opening_remaining > 0:
                    opening_remaining -= 1
                else:
                    invalid_closing += 1

        # invalid closing
        closing_remaining = 0
        for idx in reversed(range(len(s))):
            if s[idx] == ")":
                closing_remaining += 1
            elif s[idx] == "(":
                if closing_remaining > 0:
                    closing_remaining -= 1
                else:
                    invalid_opening += 1

        return (invalid_opening, invalid_closing)

    def is_valid(self, s):
        opening_count = 0

        for par in s:
            if par == "(":
                opening_count += 1
            elif par == ")":
                if opening_count == 0:
                    return False
                opening_count -= 1

        return opening_count == 0


""" 
Time Complexity :  O(2^N) 
    Since in the worst case we will have only left parentheses in the expression 
        and for every bracket we will have two options i.e. whether to remove it or consider it. 
    Considering that the expression has N parentheses, the time complexity will be O(2^N) 
Space Complexity : O(N) 
    because we are resorting to a recursive solution and for a recursive solution there is always stack space used as internal function states are saved onto a stack during recursion. 
    The maximum depth of recursion decides the stack space used. 
    Since we process one character at a time and the base case for the recursion is when we have processed all of the characters of the expression string, the size of the stack would be O(N). 
    Note that we are not considering the space required to store the valid expressions. We only count the intermediate space here.
"""


class Solution_:
    def removeInvalidParentheses(self, s):
        result = set()

        inv_opening, inv_closing = self.count_invalid(s)
        self.valid_builder(result, list(s), 0, inv_opening, inv_closing)

        return list(result)

    def valid_builder(self,  result, curr, idx, inv_opening, inv_closing):
        if idx == len(curr):
            if inv_opening == 0 and inv_closing == 0 and self.is_valid(curr):
                result.add("".join(curr))
            return
        char = curr[idx]

        # can remove opening
        if char == "(" and inv_opening > 0:
            curr[idx] = ""
            self.valid_builder(
                result, curr, idx+1, inv_opening-1, inv_closing)
            curr[idx] = "("
        # can remove closing
        if char == ")" and inv_closing > 0:
            curr[idx] = ""
            self.valid_builder(
                result, curr, idx+1, inv_opening, inv_closing-1)
            curr[idx] = ")"

        # leave it in / add regardless
        self.valid_builder(
            result, curr, idx+1, inv_opening, inv_closing)

    def count_invalid(self, s):
        inv_closing = 0
        inv_opening = 0

        # invalid closing
        opening_remaining = 0
        for char in s:
            if char == "(":
                opening_remaining += 1
            elif char == ")":
                if opening_remaining > 0:
                    opening_remaining -= 1
                else:
                    inv_closing += 1

        # invalid closing
        closing_remaining = 0
        for idx in reversed(range(len(s))):
            if s[idx] == ")":
                closing_remaining += 1
            elif s[idx] == "(":
                if closing_remaining > 0:
                    closing_remaining -= 1
                else:
                    inv_opening += 1

        return (inv_opening, inv_closing)

    def is_valid(self, s):
        opening_count = 0

        for par in s:
            if par == "(":
                opening_count += 1
            elif par == ")":
                if opening_count == 0:
                    return False
                opening_count -= 1

        return opening_count == 0


""" 

"""
