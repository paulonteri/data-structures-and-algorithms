""" 
211. Design Add and Search Words Data Structure:

Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
    

Example:
    Input
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output
        [null,null,null,null,false,true,true,true]
    Explanation
        WordDictionary wordDictionary = new WordDictionary();
        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        wordDictionary.search("pad"); // return False
        wordDictionary.search("bad"); // return True
        wordDictionary.search(".ad"); // return True
        wordDictionary.search("b.."); // return True

https://leetcode.com/problems/design-add-and-search-words-data-structure
"""


class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def addWord(self, word: str):
        curr_root = self.root
        for char in word:
            if char not in curr_root:
                curr_root[char] = {}
            curr_root = curr_root[char]
        curr_root[self.end_symbol] = True

    def search(self, word: str):
        return self.search_helper(word, 0, self.root)

    def search_helper(self, word, idx, curr_root):
        # end of word
        if idx == len(word):
            return self.end_symbol in curr_root
        # no matching char
        if word[idx] != "." and word[idx] not in curr_root:
            return False

        if word[idx] == ".":
            for letter in curr_root:
                if letter != self.end_symbol and self.search_helper(word, idx+1, curr_root[letter]):
                    return True
            return False
        else:
            return self.search_helper(word, idx+1, curr_root[word[idx]])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
