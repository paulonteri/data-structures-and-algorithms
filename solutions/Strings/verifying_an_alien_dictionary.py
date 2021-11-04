""" 
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, 
    return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: 
        The first three characters "app" match, and the second string is shorter (in size.) 
        According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

https://leetcode.com/problems/verifying-an-alien-dictionary
"""


class Solution:
    def isAlienSorted(self, words, order):

        order_dict = {order[idx]: idx for idx in range(len(order))}
        for idx in range(1, len(words)):
            if words[idx-1] == words[idx]:
                continue

            if not self.are_in_order(words[idx-1], words[idx], order_dict):
                return False

        return True

    def are_in_order(self, one, two, order_dict):
        one_idx = 0
        two_idx = 0

        # skip similar characters
        while one[one_idx] == two[two_idx]:
            # cannot move forward
            if one_idx == len(one)-1:
                return True
            elif two_idx == len(two)-1:
                return False
            # move forward
            else:
                one_idx += 1
                two_idx += 1

        return order_dict[one[one_idx]] < order_dict[two[two_idx]]
