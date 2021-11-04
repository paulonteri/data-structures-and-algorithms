""" 
Underscorify Substring:

Write a function that takes in two strings: a main string and a potential substring of the main string. 
The function should return a version of the main string with every instance of the substring in it wrapped between underscores.
If two or more instances of the substring in the main string overlap each other or sit side by side, 
    the underscores relevant to these substrings should only appear on the far left of the leftmost substring 
    and on the far right of the rightmost substring. If the main string doesn't contain the other string at all, 
    the function should return the main string intact.

Sample Input
    string = "testthis is a testtest to see if testestest it works"
    substring = "test"
Sample Output
    "_test_this is a _testtest_ to see if _testestest_ it works"
"""


def merge_positions(positions):
    merged_indices = []
    idx = 0
    while idx < len(positions):
        start, end = positions[idx]
        # # merge overlaps
        # +1 to handle side by side versions too (positions[idx][1]+1)
        while idx+1 < len(positions) and positions[idx][1]+1 >= positions[idx+1][0]:
            end = positions[idx+1][1]
            idx += 1

        merged_indices.append([start, end])
        idx += 1
    return merged_indices


def is_substring_match(string, substring, idx):
    for i, char in enumerate(substring):
        string_idx = idx + i
        if string_idx >= len(string) or string[string_idx] != char:
            return False
    return True


def find_substring_positions(string, substring):
    indices = []
    for idx in range(len(string)):
        if is_substring_match(string, substring, idx):
            indices.append([idx, idx+len(substring)-1])
    return merge_positions(indices)


def underscorifySubstring(string, substring):
    res = []

    substring_positions = find_substring_positions(string, substring)
    substring_pos_idx = 0

    for idx, char in enumerate(string):
        # cannot add an underscore
        if substring_pos_idx >= len(substring_positions):
            res.append(char)
            continue

        # add underscore
        start, end = substring_positions[substring_pos_idx]
        if start == idx and end == idx:  # len(substring) == 1
            res.append('_')
            res.append(char)
            res.append('_')
            substring_pos_idx += 1
        elif end == idx:  # end of substring
            res.append(char)
            res.append('_')
            substring_pos_idx += 1
        elif start == idx:  # beginning of substring
            res.append('_')
            res.append(char)
        else:  # cannot add
            res.append(char)

    return "".join(res)
