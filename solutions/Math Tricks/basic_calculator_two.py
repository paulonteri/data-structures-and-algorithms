"""
Basic Calculator II:

Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
    Input: s = "3+2*2"
    Output: 7
Example 2:
    Input: s = " 3/2 "
    Output: 1
Example 3:
    Input: s = " 3+5 / 2 "
    Output: 5

https://leetcode.com/problems/basic-calculator-ii/
"""


import math
"""
-------------------------- PROBLEM ----------------------------------
string s which represents an expression, evaluate this expression and return its value
not allowed to use any built-in function which evaluates strings as mathematical expressions
integer division should truncate toward zero.
s represents a valid expression
s consists of integers and operators ('+', '-', '*', '/')


-------------------------- EXAMPLES ----------------------------------
D/MA/S

"1+2"   => 3
"3+2*2" => 3+4 = 7
"5/2+3" => 2+3 = 5
"3+5/2" => 3+2 = 5
"3+5/2+5/2" => 3+2+2 = 7


-------------------------- BRUTE FORCE ----------------------------------
O(n^2) time | O(1) time 
-  evaluate each of DMAS and add it back to the string
    - do division, add it back to the string
    - multiplication...
    
-------------------------- OPTIMAL ----------------------------------

-------------------------- ONE
O(n) time | O(1) time 

- separate the s into an array that contain intergers and the signs

-  evaluate each of D/MA/S and add it to an array
    - do division on array, add the results to after_div array
    - do multiplication on after_div, add the results to after_mult array
    - do addition on after_mult...
    
-------------------------- TWO:

stack = [0]
current_number = ""
prev_operand = "+"

# deal with * and /:
- iterate through the array:
    - try to build up a number while the characters are numeric
    - if you get to a sign:
        - if the prev_operand is * or / :
            - get the currentNumber and the prevNumber and apply the prev_operand on them then add the result to the stack
        - if the prev_operand is -:
            - add neg the number to the stack
        - if the prev_operand is +:
            - add the number to the stack

        - record the new prev_operand
        - reset current_number = ""
- add all the number in the stack


"""


""" 
------------------------------------------------------------------------------------------
"""


class Solution1:
    def calculate(self, s: str):

        # separate the s into an array that contain integers and the signs
        arr = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                end = i
                while end+1 < len(s) and s[end+1].isnumeric():
                    end += 1
                arr.append(int(s[i:end+1]))
                i = end + 1
            elif s[i] == " ":
                i += 1
            else:
                arr.append(s[i])
                i += 1

        # division or multiplication
        after_dm = []
        i = 0
        while i < len(arr):
            # check for division
            if arr[i] == "/":
                after_dm[-1] = after_dm[-1] // arr[i+1]
                i += 2
            # check for multiplication
            elif arr[i] == "*":
                after_dm[-1] = after_dm[-1] * arr[i+1]
                i += 2
            else:
                after_dm.append(arr[i])
                i += 1

        # addition or subtraction
        after_sa = []
        i = 0
        while i < len(after_dm):
            # check for subtraction
            if after_dm[i] == "-":
                after_sa[-1] = after_sa[-1] - after_dm[i+1]
                i += 2
            # check for addition
            elif after_dm[i] == "+":
                after_sa[-1] = after_sa[-1] + after_dm[i+1]
                i += 2
            else:
                after_sa.append(after_dm[i])
                i += 1

        return "".join([str(item) for item in after_sa])


""" 
------------------------------------------------------------------------------------------
"""


class Solution2:
    def calculate(self, s: str):

        # separate the s into an array that contain integers and the signs
        arr = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                end = i
                while end+1 < len(s) and s[end+1].isnumeric():
                    end += 1
                arr.append(s[i:end+1])
                i = end + 1
            elif s[i] == " ":
                i += 1
            else:
                arr.append(s[i])
                i += 1

        stack = []
        current_number = ""
        prev_operand = "+"

        # evaluate addition or subtraction
        for idx in range(len(arr)+1):
            if idx < len(arr) and arr[idx].isnumeric():
                current_number = arr[idx]
                continue

            if prev_operand == "-":
                stack.append(-int(current_number))

            elif prev_operand == "+":
                stack.append(int(current_number))

            elif prev_operand == "*":
                prev_num = stack.pop()
                stack.append(prev_num * int(current_number))

            elif prev_operand == "/":
                prev_num = stack.pop()
                stack.append(math.trunc(prev_num / int(current_number)))

            if idx < len(arr):
                prev_operand = arr[idx]

        number = 0
        while stack:
            number += stack.pop()

        return number


""" 

"""


class Solution3:
    def calculate(self, s: str):

        # separate the s into an array that contain integers and the signs
        arr = []
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                end = i
                while end+1 < len(s) and s[end+1].isnumeric():
                    end += 1
                arr.append(s[i:end+1])
                i = end + 1
            elif s[i] == " ":
                i += 1
            else:
                arr.append(s[i])
                i += 1

        stack = []
        # evaluate addition or subtraction
        for idx in range(len(arr)):
            if not arr[idx].isnumeric():
                continue

            current_number = arr[idx]
            # ignore first number
            if idx == 0:
                stack.append(int(current_number))
                continue

            prev_operand = arr[idx-1]

            if prev_operand == "-":
                stack.append(-int(current_number))

            elif prev_operand == "+":
                stack.append(int(current_number))

            elif prev_operand == "*":
                prev_num = stack.pop()
                stack.append(prev_num * int(current_number))

            elif prev_operand == "/":
                prev_num = stack.pop()
                stack.append(math.trunc(prev_num / int(current_number)))

            if idx < len(arr):
                prev_operand = arr[idx]

        number = 0
        while stack:
            number += stack.pop()

        return number
