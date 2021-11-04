""" 
Interleaving String/Interweaving Strings:

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
Example 2:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
Example 3:
    Input: s1 = "", s2 = "", s3 = ""
    Output: true

https://www.algoexpert.io/questions/Interweaving%20Strings
https://leetcode.com/problems/interleaving-string/
https://leetcode.com/problems/interleaving-string/discuss/326347/C-dynamic-programming-practice-in-August-2018-with-interesting-combinatorics-warmup
"""

""" 
------------------------------------------------------------------------------------------------------------------------------------------------------
"""


def interweavingStringsBF_(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    return interweavingStringsHelperBF_(one, two, three, 0, 0, 0)


def interweavingStringsHelperBF_(one, two, three, one_idx, two_idx, three_idx):
    if three_idx == len(three):
        return True

    one_res = False
    two_res = False
    if one_idx < len(one) and one[one_idx] == three[three_idx]:
        one_res = interweavingStringsHelperBF_(
            one, two, three, one_idx+1, two_idx, three_idx+1)

    if two_idx < len(two) and two[two_idx] == three[three_idx]:
        two_res = interweavingStringsHelperBF_(
            one, two, three, one_idx, two_idx+1, three_idx+1)

    return one_res or two_res


""" 
BF that can be cached
"""


def interweavingStringsBF(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    return interweavingStringsHelperBF(one, two, three, 0, 0)


def interweavingStringsHelperBF(one, two, three, one_idx, two_idx, ):
    three_idx = one_idx + two_idx
    if three_idx == len(three):
        return True

    one_res = False
    two_res = False
    if one_idx < len(one) and one[one_idx] == three[three_idx]:
        one_res = interweavingStringsHelperBF(
            one, two, three, one_idx+1, two_idx)

    if two_idx < len(two) and two[two_idx] == three[three_idx]:
        two_res = interweavingStringsHelperBF(
            one, two, three, one_idx, two_idx+1)

    return one_res or two_res


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------
"""


def interweavingStringsMEMO(one, two, three):
    if len(three) != len(one) + len(two):

        return False
    cache = [[None for _ in range(len(two)+1)] for _ in range(len(one)+1)]
    return interweavingStringsHelperMEMO(one, two, three, cache, 0, 0)


def interweavingStringsHelperMEMO(one, two, three, cache, one_idx, two_idx, ):
    three_idx = one_idx + two_idx
    if three_idx == len(three):
        return True
    if cache[one_idx][two_idx] is not None:
        return cache[one_idx][two_idx]

    one_res = False
    two_res = False
    if one_idx < len(one) and one[one_idx] == three[three_idx]:
        one_res = interweavingStringsHelperMEMO(
            one, two, three, cache, one_idx+1, two_idx)

    if two_idx < len(two) and two[two_idx] == three[three_idx]:
        two_res = interweavingStringsHelperMEMO(
            one, two, three, cache, one_idx, two_idx+1)

    cache[one_idx][two_idx] = one_res or two_res
    return cache[one_idx][two_idx]


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------

Bottom up:

- for each char(in one or two) check if it matches what is in three:
    - if it does: if we had built the prev string up to that point == True (
            one idx behind the curr idx in three (up or left depending on if the row or column matches) )
        - then True

# can be optimised to 1D array
"""


def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    dp = [[False for _ in range(len(two)+1)] for _ in range(len(one)+1)]

    # # fill in the defaults that will be used to generate the next
    dp[0][0] = True
    for i in range(1, len(one)+1):  # left column
        actual_idx = i-1
        if one[actual_idx] == three[actual_idx] and dp[i-1][0] == True:
            dp[i][0] = True
    for i in range(1, len(two)+1):  # top row
        actual_idx = i-1
        if two[actual_idx] == three[actual_idx] and dp[0][i-1] == True:
            dp[0][i] = True

    # # fill in the rest
    for one_idx in range(1, len(one)+1):
        for two_idx in range(1, len(two)+1):
            actual_one_idx = one_idx-1
            actual_two_idx = two_idx-1
            actual_three_idx = one_idx + two_idx - 1

            # # check if the string matches then check if we had built it successfully up to that point
            # check one
            if one[actual_one_idx] == three[actual_three_idx] and dp[one_idx-1][two_idx] == True:
                dp[one_idx][two_idx] = True
            # check two
            if two[actual_two_idx] == three[actual_three_idx] and dp[one_idx][two_idx-1] == True:
                dp[one_idx][two_idx] = True

    return dp[-1][-1]
