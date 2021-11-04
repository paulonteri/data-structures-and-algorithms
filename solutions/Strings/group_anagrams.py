"""
Group Anagrams:

Write a function that takes in an array of strings and groups anagrams together.
Anagrams are strings made up of exactly the same letters, where order doesn't matter. 
For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.
Your function should return a list of anagram groups in no particular order.

Sample Input
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
Sample Output
    [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]

https://www.algoexpert.io/questions/Group%20Anagrams
https://leetcode.com/problems/group-anagrams/
"""

"""
solution for groupAnagrams1:
1. create new array sorted_words with each string sorted in alphabetical order
2. create new array sorted_idxs with sorted_words indexes
3. sort sorted_idxs by the alphabetical order of the words in sorted_words
4. you have the sorted_words in alphabetical order...
- iterate though the sorted indeces grouping words that match together 

words =        ['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']
sorted_words = ['oy', 'act', 'flop', 'act', 'foo', 'act', 'oy', 'flop']
sorted_idxs =  [0, 1, 2, 3, 4, 5, 6, 7]
sorted_idxs =  [1, 3, 5, 2, 7, 4, 0, 6]
"""


# O(w * n * log(n) + n * w * log(w)) time | O(wn) space
#   - where w is the number of words and n is the length of the longest word
def groupAnagrams1(words):

    sorted_words = []
    for word in words:
        sorted_words.append("".join(sorted(word)))

    sorted_idxs = list(range(len(words)))

    sorted_idxs.sort(key=lambda idx: sorted_words[idx])

    anagrams = []
    idx = 0
    while idx < len(sorted_idxs):
        group = [words[sorted_idxs[idx]]]
        idx += 1

        while idx < len(sorted_idxs) and sorted_words[sorted_idxs[idx]] == sorted_words[sorted_idxs[idx-1]]:

            group.append(words[sorted_idxs[idx]])
            idx += 1

        anagrams.append(group)

    return anagrams


"""
solution for groupAnagrams2 & groupAnagrams:
1. create new array sorted_words with each string sorted in alphabetical order

   create a store hashmap b4 2
2. iterate through sorted_words checking if we have seen it before 
   if not:
        add it to the store atoring its index in an array which will be its value in the hasmap
   else:
       add it's index to the array that is it's value in the store
3. for each key in the store genarate its respective strings from the keys in the array


words =        ['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']
sorted_words = ['oy', 'act', 'flop', 'act', 'foo', 'act', 'oy', 'flop']

"""


def groupAnagrams2(words):

    sorted_words = []
    for word in words:
        sorted_words.append("".join(sorted(word)))

    store = {}
    for idx, word in enumerate(sorted_words):
        if word in store:
            store[word] = store[word] + [idx]
        else:
            store[word] = [idx]

    anagrams = []
    for key in store:

        group = []
        for idx in store[key]:
            group.append(words[idx])
        anagrams.append(group)

    return anagrams


# O(w * n * log(n)) time | O(wn) space - where w is the number of words and n is the length of the longest word
def groupAnagrams(words):

    store = {}

    for string in words:
        sorted_string = "".join(sorted(string))

        if sorted_string in store:
            store[sorted_string] = store[sorted_string] + [string]
        else:
            store[sorted_string] = [string]

    return list(store.values())


print(groupAnagrams(['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']))
print(groupAnagrams2(['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']))
print(groupAnagrams1(['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']))
