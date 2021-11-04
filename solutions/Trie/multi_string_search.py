""" 
Multi String Search:

Write a function that takes in a big string and an array of small strings, all of which are smaller in length than the big string. 
The function should return an array of booleans, where each boolean represents whether the small string at that index in the array of small strings is contained in the big string.
Note that you can't use language-built-in string-matching methods.

Sample Input #1
    bigString = "this is a big string"
    smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
Sample Output #1
    [true, false, true, true, false, true, false]
Sample Input #2
    bigString = "abcdefghijklmnopqrstuvwxyz"
    smallStrings = ["abc", "mnopqr", "wyz", "no", "e", "tuuv"]
Sample Output #2
    [true, true, false, true, true, false]

https://www.algoexpert.io/questions/Multi%20String%20Search
"""


endSymbol = "*"


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = endSymbol

    def add(self, word, idx):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = (word, idx)


def find_words(trie, bigString, found_words, idx):
    # # validate
    if idx == len(bigString) or bigString[idx] not in trie:
        return
    char = bigString[idx]
    curr_trie = trie[char]

    # record all words found
    if endSymbol in curr_trie:
        _, i = curr_trie[endSymbol]
        found_words[i] = True

    find_words(curr_trie, bigString, found_words, idx+1)


# O(ns + bs) time | O(ns) space
# b len(big), s len(small), n - no. of small strings,
def multiStringSearch(bigString, smallStrings):
    found_words = [False] * len(smallStrings)

    # # create trie
    trie = Trie()
    for idx, word in enumerate(smallStrings):
        trie.add(word, idx)

    # # find words
    for idx in range(len(bigString)):
        find_words(trie.root, bigString, found_words, idx)

    return found_words
