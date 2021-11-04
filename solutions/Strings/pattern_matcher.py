""" 
Pattern Matcher:

You're given two non-empty strings. 
The first one is a pattern consisting of only "x"s and / or "y"s; the other one is a normal string of alphanumeric characters. 
Write a function that checks whether the normal string matches the pattern.
A string S0 is said to match a pattern if 
    replacing all "x"s in the pattern with some non-empty substring S1 of S0 and 
    replacing all "y"s in the pattern with some non-empty substring S2 of S0 yields the same string S0.
If the input string doesn't match the input pattern, the function should return an empty array; otherwise, 
    it should return an array holding the strings S1 and S2 that represent "x" and "y" in the normal string, in that order. 
If the pattern doesn't contain any "x"s or "y"s, the respective letter should be represented by an empty string in the final array that you return.
You can assume that there will never be more than one pair of strings S1 and S2 that appropriately represent "x" and "y" in the normal string.

Sample Input
    pattern = "xxyxxy"
    string = "gogopowerrangergogopowerranger"
Sample Output
    ["go", "powerranger"]
"""

import collections
""" 

- ensure the first letter in the pattern is x
- get the count of x and y

- for lengths of x (x_len => 1 and above):
    - calculate the y_len (length):
        - (len(string) - (x_len * x_count)) / y_count
    - get the x substring:
        - [0 : (x_len - 1)]
    - get the y substring
        - [(x_len * x_count) : (y_len - 1)]
    - build a string following the pattern using the substrings made above and check if it is equivalent to the input string
"""


# O(m) time
def order_pattern(pattern):
    patternLetters = list(pattern)
    if pattern[0] == "x":
        return patternLetters
    else:
        return list(map(lambda char: "x" if char == "y" else "y", patternLetters))


# O(m) time
def get_num_x_b4_y(sorted_pattern):
    num_x_b4_y = 0
    for char in sorted_pattern:
        if char == 'y':
            break
        num_x_b4_y += 1
    return num_x_b4_y


# O(n^2 + m) time | O(n + m) space
def patternMatcher(pattern, string):
    sorted_pattern = order_pattern(pattern)
    num_x_b4_y = get_num_x_b4_y(sorted_pattern)
    count = collections.Counter(sorted_pattern)

    # # missing x or y
    if count['y'] == 0:
        if pattern[0] == 'y':
            return ['', string[:count["x"]]]
        return [string[:count["x"]], '']

    # O(n^2) time
    for x_len in range(1, len(string)):
        # # y details
        y_len = (len(string) - (x_len*count["x"])) / count["y"]
        if y_len != round(y_len):  # skip decimals
            continue
        y_len = round(y_len)
        y_start = x_len*num_x_b4_y

        # # build new string
        new_string = [""]*len(sorted_pattern)
        x_substring = string[0:x_len]
        y_substring = string[y_start:y_start+y_len]
        for idx, char in enumerate(sorted_pattern):
            if char == 'x':
                new_string[idx] = x_substring
            else:
                new_string[idx] = y_substring

        # # validate new string
        if "".join(new_string) == string:
            if pattern[0] == 'y':
                return [y_substring, x_substring]
            return [x_substring, y_substring]

    return []
