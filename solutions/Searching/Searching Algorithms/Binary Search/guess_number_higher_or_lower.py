"""
Guess Number Higher or Lower: (Binary Search)

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns 3 possible results:
    -1: The number I picked is lower than your guess (i.e. pick < num).
    1: The number I picked is higher than your guess (i.e. pick > num).
    0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.

https://leetcode.com/problems/guess-number-higher-or-lower/
"""

#
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


def guess(num: int):
    pass
#
#


class Solution:
    def guessNumber(self, n):

        if n < 2:
            return n

        left = 1
        right = n

        # we don't use left < right because: the middle pointer will never be at the right pointer,
        # so if the the number we are guessing == n, the right pointer will never be checked (right = n) and,
        # hence never find the guess number
        while left <= right:

            mid = (left+right) // 2
            guess_res = guess(mid)

            if guess_res == 0:
                return mid
            # lower
            elif guess_res == 1:
                left = mid + 1
            else:
                right = mid - 1


class Solution00:
    def guessNumber(self, x: int):

        left = 1
        right = x
        while left <= right:
            mid = (left+right) // 2
            res = guess(mid)
            # print(left, right, mid, res)

            if res == 0:
                return mid

            elif res == -1:
                right = mid - 1

            else:
                left = mid + 1


"""
[0,1,2,3,4,5,6,7,8]
[1,2,3,4,5,6,7,8,9]
6

r = 9
l = 1
m = 5

r = 9
l = 1
m = 5

"""
