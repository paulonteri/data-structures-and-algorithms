"""
Longest Palindromic Substring:

Given a string s, return the longest palindromic substring in s.
https://leetcode.com/problems/longest-palindromic-substring/
https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring
"""


class Solution:
    def longestPalindrome(self, s: str):
        if len(s) < 2:
            return s

        longest = idx = 1
        left = right = 0
        for idx in range(1, len(s)):

            # check for both even and odd palindromes
            # Examples: even -> zyaaaagh, odd -> zyaaagh
            even, left_even, right_even = self.expandFromMiddle(s, idx-1, idx)
            odd, left_odd, right_odd = self.expandFromMiddle(s, idx-1, idx+1)

            # record the largest palindrome we found
            if even > odd and even > longest:
                longest = even
                left = left_even
                right = right_even
            if odd > even and odd > longest:
                longest = odd
                left = left_odd
                right = right_odd

        return s[left:right+1]

    def expandFromMiddle(self, s, left, right):
        if right >= len(s) or s[left] != s[right]:
            return 0, left, right

        # pointers showing how far we have expanded (which marks how wide the palindrome is)
        exp_left = left
        exp_right = right

        while left >= 0 and right < len(s) and s[left] == s[right]:
            # expand
            exp_left = left
            exp_right = right

            # move on to checking the next
            left -= 1
            right += 1

        # return len of the longest palindrome we found
        return ((exp_right - exp_left) + 1), exp_left, exp_right


"""
Longest Palindromic Substring:

Write a function that, given a string, returns its longest palindromic substring.
A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.
You can assume that there will only be one longest palindromic substring.
"""


def longestPalindromicSubstring3(string):
    longest = [0, 0]

    for idx in range(1, len(string)):

        odd_checker = get_longest_palandrome(string, idx-1, idx+1)
        even_checker = get_longest_palandrome(string, idx-1, idx)

        longest = max(longest, odd_checker, even_checker,
                      key=lambda x: x[1] - x[0])

    return string[longest[0]: longest[1]+1]


def get_longest_palandrome(string, left, right):
    # validate
    if not (left >= 0 and right < len(string)) or \
        string[left] != string[right] or \
            not string[left].isalnum() or not string[right].isalnum():
        return [0, 0]

    # increase palindrome size(width)
    while left-1 >= 0 and right+1 < len(string):
        if string[left-1] != string[right+1] or \
                not string[left-1].isalnum() or not string[right+1].isalnum():
            break
        left -= 1
        right += 1

    return [left, right]
