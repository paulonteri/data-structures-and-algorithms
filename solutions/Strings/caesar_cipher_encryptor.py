"""
Caesar Cipher Encryptor:

Given a non-empty string of lowercase letters and a non-negative integer representing a key,
write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet,
where k is the key.
Note that letters should "wrap" around the alphabet;
 in other words, the letter z shifted by one returns the letter a.
https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
"""


# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):

    characters = list(string)

    # Calculate where to move the character
    for idx, char in enumerate(characters):
        char_unicode = ord(char) + key

        # make sure key is < ord('z') else subtract 26
        while char_unicode > ord('z'):
            char_unicode -= 26

        # replace moved character in our characters
        characters[idx] = chr(char_unicode)

    return "".join(characters)


def caesarCipherEncryptor_(string, key):

    letters = []
    key = key % 26  # handle large numbers
    for char in string:
        moved_ord = ord(char) + key

        if moved_ord > ord('z'):
            moved_ord -= 26

        letters.append(chr(moved_ord))

    return "".join(letters)


# O(n) time | O(n) space
def caesarCipherEncryptor1(string, key):

    newLetters = []
    newKey = key % 26  # handle large numbers

    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))

    return "".join(newLetters)


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    #                                                 # return within alphabet
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


"""
For each character in the string calculate where to move it

# convert characters/string into array for better runtime
1. Iterate through each character
2. Calculate where to move the character
    - get it's unicode value: ord(char)
    - add/move it by the key: ord(char) + key
    - make sure key is < ord('z') else subtract 26 - to return it withoin the alphabet
    - convert back to char chr(result from above) 
3. replace character in our characters
4. convert characters to string and return 

"""

print(caesarCipherEncryptor("abcxyz", 1))
print(caesarCipherEncryptor("abcxyz", 100))
