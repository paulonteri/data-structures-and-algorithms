"""
A palindrome is a string that reads the same forwards and backwards, e.g., "level", "rotator", and "foobaraboof".
Write a program to test whether the letters forming a string can be permuted to form a palindrome. For example, "edified" can be permuted to form "deified"

EPI 12.1
"""

from collections import Counter


def can_form_palindrome(s: str) -> bool:
    letter_counter = Counter(s)
    num_of_odd_appearances = sum(
        counter % 2 for counter in letter_counter.values()
    )
    return num_of_odd_appearances < 2
