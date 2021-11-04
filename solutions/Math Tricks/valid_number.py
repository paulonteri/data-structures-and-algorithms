""" 
Valid Number

A valid number can be split up into these components (in order):
    A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):
    (Optional) A sign character (either '+' or '-').
    One of the following formats:
        One or more digits, followed by a dot '.'.
        One or more digits, followed by a dot '.', followed by one or more digits.
        A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):
    (Optional) A sign character (either '+' or '-').
    One or more digits.

For example, 
    all the following are valid numbers: 
        ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
    while the following are not valid numbers: 
        ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
Given a string s, return true if s is a valid number.

Example 1:
    Input: s = "0"
    Output: true
Example 2:
    Input: s = "e"
    Output: false
Example 3:
    Input: s = "."
    Output: false
Example 4:
    Input: s = ".1"
    Output: true

https://leetcode.com/problems/valid-number
"""

from collections import Counter


# O(N) time | O(N) space
class Solution:
    def isNumber(self, s: str):
        """ 
        - verify all characters are 0-9,e,E,+,-,.
        - if has e/E's: 
            - run the verifyNumberWithEs(s)
        - else:
            - run the verifyNumberWithoutEs(s)
        """
        if not s:
            return False
        # verify all characters are 0-9,e,E,+,-,.
        for char in s:
            if not (char.isnumeric() or char in "eE+-."):
                return False
        # if has e/E's
        if 'e' in s or 'E' in s:
            return self.verifyNumberWithEs(s)
        else:
            return self.verifyNumberWithoutEs(s)

    def verifyNumberWithEs(self, s):
        """ 
        - verify e/E's 
            - only one

        - split s by the E's
            - followed by integer (not float)
            - order: [number, e, number]
                - run the verifyNumberWithoutEs() on the numbers
        """

        # only one E
        char_count = Counter(s)
        if char_count['e'] + char_count['E'] != 1:
            return False

        # split s
        e_split = []
        if 'e' in char_count:
            e_split = s.split("e")
        else:
            e_split = s.split("E")
        if len(e_split) != 2:
            return False

        # followed by integer (not float)
        if "." in e_split[1]:
            return False

        # run the verifyNumberWithoutEs() on the numbers
        return self.verifyNumberWithoutEs(e_split[0]) and self.verifyNumberWithoutEs(e_split[1])

    def verifyNumberWithoutEs(self, s):
        """ 
        Checks if a number is valid without considering e/E's
        - has numeric characters
        - check if has zero or one of -,+ at the beginning and remove it
        - check if has zero or one of .
            - verify . has digits on either side
        """
        char_count = Counter(s)

        # has numeric characters
        if not self.has_numeric_chars(s):
            return False

        # check if has zero or one of -,+ at the beginning and remove it
        sign_count = char_count['+'] + char_count['-']
        if not (sign_count == 1 or sign_count == 0):
            return False
        s_wo_signs = s
        if sign_count:
            s_wo_signs = s[1:]
            if not self.has_numeric_chars(s_wo_signs):
                return False
            if '+' in s_wo_signs or '-' in s_wo_signs:
                return False

        # check if has zero or one of .
        if not (char_count['.'] == 1 or char_count['.'] == 0):
            return False
        # verify . has digits on either side
        dot_split = s_wo_signs.split('.')
        if not self.has_numeric_chars(dot_split[0]) and not self.has_numeric_chars(dot_split[1]):
            return False

        return True

    def has_numeric_chars(self, s):
        for char in s:
            if char.isnumeric():
                return True
        return False


""" 
Constant space

"""


# O(N) time | O(1) space
class Solution_:
    def isNumber(self, s: str):
        """ 
        Digits
            - must exist
        Signs
            - one on either side of exponent
            - at beginning of string or just after exponent
            - must have digits after it
        Exponents
            - must have digits b4 & after it
            - can only be one
        Dots
            - cannot be after exponent
                - can be only on left side of exponent
                - max of one
            - digit on either side
        Anything else
            - invalid input
        """

        seen_digit = False
        seen_exponent = False
        seen_dot = False
        for idx, char in enumerate(s):
            # 0-9
            if char.isnumeric():
                seen_digit = True

            # "+-" one on either side of exponent
            # can be at beginning of string or just after exponent & must have digits after it
            elif char in "+-":
                if not (idx == 0 or s[idx-1] in "eE") or idx == len(s)-1:
                    return False

            # "eE" - must have digits b4 & after it & can only be one
            elif char in "eE":
                if not seen_digit or seen_exponent or idx == len(s)-1:
                    return False
                seen_exponent = True

            # "." max of one & can be only on left side of exponent & digit on either side
            elif char == ".":
                # max of one & can be only on left side of exponent
                if seen_dot or seen_exponent:
                    return False
                # digit on either side
                has_left_digit = False
                has_right_digit = False
                if idx > 0 and s[idx-1].isnumeric():
                    has_left_digit = True
                if idx < len(s)-1 and s[idx+1].isnumeric():
                    has_right_digit = True

                if not (has_left_digit or has_right_digit):
                    return False
                seen_dot = True

            # invalid character
            else:
                return False

        # digits must exist
        return seen_digit


""" 
test cases:
    "2"
    "0089"
    "-0.1"
    "+3.14"
    "4."
    "-.9"
    "2e10"
    "-90E3"
    "3e+7"
    "+6e-1"
    "53.5e93"
    "-123.456e789"
    "abc"
    "1a"
    "1e"
    "e3"
    "99e2.5"
    "--6"
    "-+3"
    "95a54e53"
"""
