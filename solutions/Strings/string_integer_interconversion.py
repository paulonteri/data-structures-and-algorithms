"""
Interconvert Strings & Integers:

A string is a sequence of characters. A string may encode an integer, e.g., "123" encodes 123. 
In this problem, you are to implement methods that take a string representing an integer and return the corresponding integer, and vice versa. 
Your code should handle negative integers. You cannot use library functions like int in Python.
Implement an integer to string conversion function, and a string to integer conversion function, 
For example, 
 if the input to the first function is the integer 314,
 it should return the string "314" 
 and if the input to the second function is the string "314" it should return the integer 314.

EPI 6.1
"""


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
int to string
"""


def single_digit_to_char(digit):
    return chr(ord('0')+digit)


def int_to_string(x: int):
    if x == 0:
        return "0"

    is_neg = False
    if x < 0:
        is_neg, x = True, -x

    result = []
    while x > 0:
        result.append(single_digit_to_char(x % 10))
        x = x // 10

    if is_neg:
        result.append('-')
    return "".join(reversed(result))


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
string to int
"""


def single_char_to_int(character):
    num_mapping = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }
    return num_mapping[character]


def string_to_int(s: str):

    is_neg = False
    start_idx = 0
    if s and s[0] == "-":
        is_neg, start_idx = True, 1
    if s and s[0] == "+":
        start_idx = 1

    running_sum = 0
    multiplier = 1

    for idx in reversed(range(start_idx, len(s))):
        running_sum += single_char_to_int(s[idx])*multiplier
        multiplier *= 10

    if is_neg:
        return -running_sum
    return running_sum
