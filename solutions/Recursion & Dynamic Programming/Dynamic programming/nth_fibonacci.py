"""
Nth Fibonacci:

The Fibonacci sequence is defined as follows: 
 the first number of the sequence is 0, the second number is 1,
 and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. 
Write a function that takes in an integer n and returns the nth Fibonacci number.
Important note: the Fibonacci sequence is often defined with its first two numbers 
 as F0 = 0 and F1 = 1. For the purpose of this question, the first Fibonacci number is F0;
  therefore, getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc..

    Sample Input #1
    n = 2
    Sample Output #1
    1 // 0, 1

https://www.algoexpert.io/questions/Nth%20Fibonacci
"""
# {1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 8, 8: 13}


# O(2^n) time | O(n) space
def getNthFib00(n):
    if n == 2:
        return 1

    if n == 1:
        return 0

    return getNthFib00(n-1) + getNthFib00(n-2)


# O(n) time | O(n) space
def getNthFib01(n):
    store = {1: 0, 2: 1}
    return getNthFibHelper01(n, store)


def getNthFibHelper01(n, store):
    if n in store:
        return store[n]

    store[n] = getNthFibHelper01(n-1, store) + getNthFibHelper01(n-2, store)
    return store[n]


# 0(n) time | 0(1) space
def getNthFib(n):
    if n == 1:
        return 0

    # getNthFib(2) = getNthFib(2) + getNthFib(1)
    prev_f = 0
    curr_f = 1
    num = 2

    # getNthFib(3) = getNthFib(2) + getNthFib(1)
    # getNthFib(3) = curr_f + prev_f
    while num < n:
        new_prev_f = curr_f
        new_curr_f = curr_f + prev_f

        curr_f, prev_f = new_curr_f, new_prev_f

        num += 1

    return curr_f
