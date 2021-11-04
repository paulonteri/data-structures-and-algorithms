"""
Max Substring Alphabetically
Given a string, determine the maximum alphabetically, substring
"""


def maxSubstring(s):

    if len(s) < 1:
        return ""

    # get all characters' indexes
    # sort characters alphabetically
    characters = []  # ['a', 'p', 'l', 'e']
    idx_store = {}  # {'a': [0], 'p': [1, 2], 'l': [3], 'e': [4]}
    for idx, char in enumerate(s):
        if char not in idx_store:
            characters.append(char)
            idx_store[char] = [idx]
        else:
            idx_store[char].append(idx)

    characters.sort()
    # handle the last character's (from characters array) substrings only
    last_char = characters[-1]

    # get all substrings starting with the last character
    # sort them
    substrings = []  # ['p', 'pp', 'ppl', 'pple', 'p', 'pl', 'ple']
    for idx in idx_store[last_char]:
        right = idx
        while right < len(s):
            substrings.append(s[idx:right+1])
            right += 1

    substrings.sort()
    return substrings[-1]  # pple


print(maxSubstring("apple"))
print(maxSubstring("apsgsxvbbdbsdbsdknnple"))
print(maxSubstring("asazsxs"))
print(maxSubstring("as"))
print(maxSubstring("applze"))
print(maxSubstring("azpple"))
print(maxSubstring("apzzple"))

# Not on Leetcode
