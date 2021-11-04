"""
Reverse Words in a String:

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Reverse Words In String:
Write a function that takes in a string of words separated by one or more whitespaces and returns a string that has these words in reverse order.
For example, given the string "tim is great", your function should return "great is tim".
For this problem, a word can contain special characters, punctuation, and numbers.
The words in the string will be separated by one or more whitespaces, and the reversed string must contain the same whitespaces as the original string.
For example, given the string "whitespaces 4" you would be expected to return "4 whitespaces".
Note that you're not allowed to to use any built-in split or reverse methods/functions. However, you are allowed to use a built-in join method/function.
Also note that the input string isn't guaranteed to always contain words.

Sample Input
    string = "AlgoExpert is the best!"
Sample Output
    "best! the is AlgoExpert"

https://leetcode.com/problems/reverse-words-in-a-string/
https://www.algoexpert.io/questions/Reverse%20Words%20In%20String
"""


class Solution:
    def reverseWords(self, s: str):

        start = 0
        output = []
        while start < len(s):
            # skip whitepace
            while start < len(s) and s[start] == ' ':
                start += 1

            if start < len(s):

                end = start
                while end < len(s) and s[end] != ' ':  # find entire word
                    end += 1

                # add word to output
                if len(output) == 0:
                    output.append(s[start:end])
                else:
                    output.append(' ')
                    output.append(s[start:end])
                start = end

        output.reverse()
        return "".join(output)

    def reverseWords2(self, s: str):
        # reversed_words = s.split()[::-1]
        # return " ".join(reversed_words)
        return " ".join(s.split()[::-1])


# O(n) time | O(n) space - where n is the length of the string
def reverseWordsInString(string):
    words = []

    idx = len(string) - 1
    while idx >= 0:
        # white space
        if string[idx] == " ":
            words.append(" ")
            idx -= 1

        # words
        else:
            # get word's beginning
            start = idx
            while start - 1 >= 0 and string[start - 1] != " ":
                start -= 1
            # add word to words array
            words.append(string[start:idx+1])

            idx = start - 1
    return "".join(words)
