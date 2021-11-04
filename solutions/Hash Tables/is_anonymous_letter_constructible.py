"""
Write a program which takes text for an anonymous letter and text for a magazine and 
 determines if it is possible to write the anonymous letter using the magazine.
The anonymous letter can be written using the magazine if for each character in the anonymous letter, 
 the number of times it appears in the anonymous letter is no more than the number of times it appears in the magazine.

EPI 12.2
"""

from collections import Counter


# O(m+n) time | O(1) space since there are limited characters
def is_letter_constructible_from_magazine0(letter_text: str,
                                           magazine_text: str):
    letter_chars = Counter(letter_text)
    magazine_chars = Counter(magazine_text)

    for char in letter_chars:

        if letter_chars[char] > magazine_chars[char]:
            return False

    return True


# O(m+n) time | O(1) space since there are limited characters
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str):
    magazine_chars = Counter(magazine_text)

    for char in letter_text:
        magazine_chars[char] -= 1

        if magazine_chars[char] < 0:
            return False

    return True
