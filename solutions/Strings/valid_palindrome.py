"""
Valid Palindrome:

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


# O(n) time | O(1) space 🥵🥵 | n = len(s)
class Solution:
    def isPalindrome(self, s: str):

        # we will start be comparing the left most char & the right most char
        a_pointer = 0
        b_pointer = len(s) - 1

        while a_pointer < b_pointer:

            # skip non alphanumeric
            while a_pointer < b_pointer and not s[a_pointer].isalnum():
                a_pointer += 1
            while a_pointer < b_pointer and not s[b_pointer].isalnum():
                b_pointer -= 1

            # check if not the same
            if s[a_pointer].lower() != s[b_pointer].lower():
                return False  # if we find a duo that doesn't match

            # move on to the next set of chars
            a_pointer += 1
            b_pointer -= 1

        return True


"""
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

"""


"""
Palindrome Check:

Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.
https://www.algoexpert.io/questions/Palindrome%20Check
"""


# 0(n) time | O(1) space - where n = len(string)
def isPalindrome(string):

    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True


"""
Sample Input
    string = "abcdcba"
Sample Output
    true // it's written the same forward and backward

# input: valid string
# output: true/false boolean
# edge-cases:
    - one charactter string is a valid palindrome

# # First Approach: 0(n) time | O(n) space - where n = len(string)
# reverse string then
# compare if reversed string == original string

# # Second approach: 
- have two pointers at the opposite ends of the string
# move them inwards by one and check (while left <= right):
    - if the char at the left pointer != char at the left pointer, return False
    - if the char at the left pointer == char at the left pointer, repeat this current step
# return True // we didn't find any problem

def isPalindrome(string):
     left = 0
     right = len(string) - 1
     while left <= right:
         if string[left] != string[right]:
             return False
         left += 1
         right -= 1

     return True

"""


# Recursive
# O(n) time | O(n) space
def isPalindromeStr(string, start=0):

    end = len(string) - 1 - start

    if start >= end:
        return True

    return string[start] == string[end] and isPalindromeStr(string, start+1)
