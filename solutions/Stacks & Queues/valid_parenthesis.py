"""
Valid Parentheses / Balanced Brackets

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


https://leetcode.com/problems/valid-parentheses/
https://www.algoexpert.io/questions/Balanced%20Brackets
"""


class Solution(object):
    def isValid(self, s):

        myStack = []

        match = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for par in s:
            if par == "(" or par == "{" or par == "[":
                myStack.append(par)

            elif len(myStack) == 0 or match[myStack.pop()] != par:
                return False

        return len(myStack) == 0


def balancedBrackets(string):
    opening_brackets = "([{"
    matching_brackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:

        if char not in matching_brackets and char in opening_brackets:  # opening bracket
            stack.append(char)

        # closing brackets
        elif char in matching_brackets and(not stack or matching_brackets[char] != stack.pop(-1)):
            return False

    return len(stack) == 0


print(balancedBrackets("([])(){}(())()()"))
print(balancedBrackets("([])(){}(()))()()"))
