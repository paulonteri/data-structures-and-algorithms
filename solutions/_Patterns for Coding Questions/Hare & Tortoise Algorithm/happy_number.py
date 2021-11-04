"""
Happy Number:

Any number will be called a happy number if,
after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’.
All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:
    Input: n = 19
    Output: true
    Explanation:
        12 + 92 = 82
        82 + 22 = 68
        62 + 82 = 100
        12 + 02 + 02 = 1
Example 2:
    Input: n = 2
    Output: false
Example 3:
    Input: 23
    Output: true (23 is a happy number)
    Explanations: Here are the steps to find out that 23 is a happy number:
Example 4:
    Input: 12
    Output: false (12 is not a happy number)
    Explanations: Here are the steps to find out that 12 is not a happy number:

https://leetcode.com/problems/happy-number/
https://www.educative.io/courses/grokking-the-coding-interview/39q3ZWq27jM
"""


def square_of_digits(num):
    res = 0
    while num > 0:
        res += (num % 10) * (num % 10)
        num = num // 10
    return res


def find_happy_number(num):
    fast = num
    slow = num
    loop_started = False
    while slow != fast or not loop_started:
        loop_started = True
        fast = square_of_digits(square_of_digits(fast))
        slow = square_of_digits(slow)
        if slow == 1 or fast == 1:
            return True

    return False


# using memory
def find_happy_number_01(num):
    store = set()
    store.add(num)
    while num != 1:
        num = square_of_digits(num)
        if num in store:
            return False
        store.add(num)

    return True
