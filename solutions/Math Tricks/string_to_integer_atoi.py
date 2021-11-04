"""
String to Integer (atoi):

Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number,
 or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231 is returned.
https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, string: str):

        idx = 0

        # skip whitespace
        while idx < len(string) and string[idx] == ' ':
            idx += 1

        # deal with number
        if idx < len(string) and (string[idx] == '-' or string[idx] == '+' or string[idx].isnumeric()):
            # find number
            start = idx
            if string[idx] == '-' or string[idx] == '+':  # handle stuff like "+-12"
                idx += 1
            while idx < len(string) and string[idx].isnumeric():
                idx += 1

            # convert into number
            if string[start] == '-':
                if idx-start == 1:
                    return 0
                return -self.convertToIntNeg(string[start+1:idx])
            elif string[start] == '+':
                if idx-start == 1:
                    return 0
                return self.convertToIntPos(string[start+1:idx])
            return self.convertToIntPos(string[start:idx])

        return 0

    def convertToIntPos(self, string):
        integer = int(string)
        if integer >= 2**31:
            return 2**31 - 1
        return integer

    def convertToIntNeg(self, string):
        integer = int(string)
        if integer >= 2**31:
            return 2**31
        return integer


"""
# Input: valid string
# Output: integer
# Assumptions:
    - some strings might start without white space
    - only ' ' is considered whitespace
    - some strings will not contain numerical digits after the whitespace
    - ignore everythong after the whitespace thet is not a -, + , or a numerical value
    - return 0 if no valis sol is found

# Examples:
'  -502apple' -> -502
'  -502 apple' -> -502
'  -502 200' -> -502
'+502 200' -> 502
'  t-502apple' -> 0

# # First Approach: 
- iterate through the string
# skip all the whitespace (while loop 1)
# check whether next character is -, +  or number: (while loop 2)
    - if not, return 0
    - if it is: continue iterating while storing all it's characters in an array ### O(1) time
# convert the stored characters into a number and return the number ### O(n) time
    - convert the array into an string (skipping -, +) then return it or negate and return it
# return 0
## time O(n) | O(n) space - where n is len(string) 

# # Second Approach:
- iterate through the string
# skip all the whitespace (while loop 1)
# check whether next character is -, +  or number: (while loop 2)
    - if not, return 0
    - if it is: continue iterating (keep track of the satrting and ending indices) ### O(1) time
# convert the found number string (we can get it using slicing) into a number and return the number ### O(n) time
    - return it or negate and return it
# return 0
## time O(n) | O(n) space - where n is len(string) 


def myAtoi(self, s: str):
    idx = 0

    # skip whitespace
    while idx < len(string) and string[idx] == ' ':
        idx += 1

    # deal with number
    if idx < len(string) and (string[idx] == '-' or string[idx] == '+' or string[idx].isnumeric())
        # find number
        start = idx
        while idx < len(string) and (string[idx] == '-' or string[idx] == '+' or string[idx].isnumeric())
            idx += 1

        # convert into number
        if string[start] == '-':
            return -int(string[start+1:idx])
        elif string[start] == '-':
            return int(string[start+1:idx])
        return int(string[start:idx])

    return 0


"""
