"""
Count Primes:

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:
    Input: n = 0
    Output: 0
Example 3:
    Input: n = 1
    Output: 0

https://leetcode.com/problems/count-primes
"""

""" 
The basic brute-force solution for this problem is to iterate from 0 to n and for each number, we do a prime-check. 
To check if a number is prime or not, we simply check if its divisors include anything other than 1 and the number itself. 
If so, then it is not a prime number. This method will not scale for the given limits on n. 
The iteration itself has O(n) time complexity and for each iteration, we have the prime check which takes O(sqrt)O( n). 
This will exceed the problem's time limit. Therefore, we need a more efficient solution.

Instead of checking if each number is prime or not, what if we mark the multiples of a prime number as non-prime?
"""




import math
class Solution_:  # times out on leetcode
    def isPrime(self, n):

        for num in range(2, math.floor(math.sqrt(n))):
            if n % num == 0:
                return False

        return True

    def countPrimes(self, n: int):
        if n <= 2:
            return 0

        numbers = [-1] * n
        numbers[0] = False
        numbers[1] = False

        for idx in range(2, n):
            if numbers[idx] == False:
                continue

            numbers[idx] = self.isPrime(idx)

            if numbers[idx]:  # only consider primes to ensure not calculating duplicates

                multiplier = idx
                while multiplier * idx < n:
                    numbers[multiplier * idx] = False
                    multiplier += 1

        return numbers.count(True)


""" 
"""


class Solution:
    def countPrimes(self, n: int):
        if n <= 2:
            return 0

        numbers = [True] * n
        numbers[0] = False
        numbers[1] = False

        for idx in range(2, n):

            if numbers[idx]:  # only consider primes to ensure not calculating duplicates

                for multiple in range(idx+idx, n, idx):  # start,stop+1,step
                    numbers[multiple] = False

        return numbers.count(True)
