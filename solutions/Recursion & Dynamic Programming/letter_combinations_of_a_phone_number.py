"""
Letter Combinations of a Phone Number:

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
"""
Phone Number Mnemonics:
If you open the keypad of your mobile phone, it'll likely look like this:

   ----- ----- -----
  |     |     |     |
  |  1  |  2  |  3  |
  |     | abc | def |
   ----- ----- -----
  |     |     |     |
  |  4  |  5  |  6  |
  | ghi | jkl | mno |
   ----- ----- -----
  |     |     |     |
  |  7  |  8  |  9  |
  | pqrs| tuv | wxyz|
   ----- ----- -----
        |     |
        |  0  |
        |     |
         -----

Almost every digit is associated with some letters in the alphabet; this allows certain phone numbers to spell out actual words.
For example, the phone number 8464747328 can be written as timisgreat; similarly, the phone number 2686463 can be written as antoine or as ant6463.
It's important to note that a phone number doesn't represent a single sequence of letters, but rather multiple combinations of letters.
For instance, the digit 2 can represent three different letters (a, b, and c).
A mnemonic is defined as a pattern of letters, ideas, or associations that assist in remembering something
Companies oftentimes use a mnemonic for their phone number to make it easier to remember.
Given a stringified phone number of any non-zero length, write a function that returns all mnemonics for this phone number, in any order.
For this problem, a valid mnemonic may only contain letters and the digits 0 and 1.
In other words, if a digit is able to be represented by a letter, then it must be. Digits 0 and 1 are the only two digits that don't have letter representations on the keypad.
Note that you should rely on the keypad illustrated above for digit-letter associations.

Sample Input
    phoneNumber = "1905"
Sample Output
    [
    "1w0j",
    "1w0k",
    "1w0l",
    "1x0j",
    "1x0k",
    "1x0l",
    "1y0j",
    "1y0k",
    "1y0l",
    "1z0j",
    "1z0k",
    "1z0l",
    ]
    // The mnemonics could be ordered differently.
https://www.algoexpert.io/questions/Phone%20Number%20Mnemonics
"""


class Solution0:
    def letterCombinations(self, digits: str):

        if not digits:
            return []

        key_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        res = ['']

        for num in digits:

            # add num's letters to all arrays in res
            temp = []

            for letter in key_map[int(num)]:
                for string in res:
                    temp.append(string + letter)

            res = temp

        return res

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


key_map = {
    0: ["0"],
    1: ["1"],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

# # # # #


def phoneNumberMnemonics00(phoneNumber):
    all_combinations = []
    phoneNumberMnemonicsHelper00(phoneNumber, 0, all_combinations, [])
    return all_combinations


def phoneNumberMnemonicsHelper00(phoneNumber, idx, all_combinations, curr_combination):

    if idx >= len(phoneNumber):
        all_combinations.append("".join(curr_combination))
        return

    letters = key_map[int(phoneNumber[idx])]
    for letter in letters:
        phoneNumberMnemonicsHelper00(
            phoneNumber, idx + 1, all_combinations, curr_combination + [letter])


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# O(4^n * n) time | O(4^n * n) space - where n is the length of the phone number
def phoneNumberMnemonics(phoneNumber):
    all_combinations = []
    curr_combination_template = list(range(len(phoneNumber)))
    phoneNumberMnemonicsHelper(
        phoneNumber, 0, all_combinations, curr_combination_template)
    return all_combinations


def phoneNumberMnemonicsHelper(phoneNumber, idx, all_combinations, curr_combination):

    if idx >= len(phoneNumber):
        all_combinations.append("".join(curr_combination))
        return

    letters = key_map[int(phoneNumber[idx])]
    for letter in letters:
        # place current letter in curr_combination and go forward to other idxs
        # we will backtrack and place the other letters too
        curr_combination[idx] = letter
        phoneNumberMnemonicsHelper(
            phoneNumber, idx + 1, all_combinations, curr_combination)
