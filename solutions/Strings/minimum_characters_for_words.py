"""
Minimum Characters For Words:

Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words.
The characters don't need to be in any particular order.
For example, the characters ["y", "r", "o", "u"] are needed to form the words ["your", "you", "or", "yo"].
Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

Sample Input
    words = ["this", "that", "did", "deed", "them!", "a"]
Sample Output
    ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
    // The characters could be ordered differently.


https://www.algoexpert.io/questions/Minimum%20Characters%20For%20Words
"""


from collections import defaultdict


# O(n) time | O(n) space - where n is the length of the word
def get_word_characters(word):
    char_count = defaultdict(int)
    for char in word:
        char_count[char] += 1

    return char_count


# O(n*l) time | O(c) space
# where n is the number of words, l the length of the longest word, c the number of unique charactters
def minimumCharactersForWords(words):
    min_character_count = defaultdict(int)

    for word in words:
        word_char_count = get_word_characters(word)
        for char in word_char_count:
            # update count if we find a word that needs more
            min_character_count[char] = max(
                min_character_count[char], word_char_count[char]
            )

    # convert hash table to list
    min_character_count_list = []
    for char in min_character_count:
        count = min_character_count[char]
        while count > 0:
            min_character_count_list.append(char)
            count -= 1

    return min_character_count_list


"""
- Draw Example(s)
- Test case
- Brute force
- Explain Solution / Algorithm
- Talk about tradeoffs
- Talk through edge cases
- Pseudocode
- Code

[
"this",  -> "t","h","i","s"
"that",  -> "t","t","h","a"
"did"    -> "d","d","i"
]

["t","t","h","i","s","d","d"]

- have an output array that will store the char count
- for each word, calculate the unique character count. Then check

def get_word_characters(word):
	return {}

def minimumCharactersForWords(words):
    min_character_count = {}
	for word in words:
		word_char_count = get_word_characters(word)
		# coompare the word_char_count & min_character_count then update if necessary
		
    return convert_to_list(min_character_count)
	
"""
