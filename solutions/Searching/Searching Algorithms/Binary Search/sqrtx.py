
"""
Sqrt(x): (Binary Search)

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
 and only the integer part of the result is returned.

Example 1:
	Input: x = 4
	Output: 2

Example 2:
	Input: x = 8
	Output: 2
	Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
https://leetcode.com/problems/sqrtx/
"""


class Solution:
    def mySqrt(self, x: int):

        left = 1
        right = x
        while left <= right:
            mid = (left+right) // 2
            mid_sq = mid * mid

            if mid_sq == x:
                return mid

            elif mid_sq > x:
                right = mid - 1

            else:
                left = mid + 1

        return (left+right) // 2


"""
[0,1,2,3,4,5,6,7,8]
[1,2,3,4,5,6,7,8,9]
9

l = 1,0
r = 9,8
mid = 5,4

l = 1,0
r = 4,3
mid = 3,2

[0,1,2,3,4,5,6,7]
[1,2,3,4,5,6,7,8]
8

l = 1,0
r = 8,7
mid = 4,3


l = 1,0
r = 3,2
mid = 2,1



"""


def mySqrt(self, x):

    if x < 2:
        return x

    left = 1
    right = x

    while left <= right and left ** 2 <= x:
        # Remember:
        # the mid can be on the left pointer, never on the right: floor division -> rounds down results
        # we want to push left as far up as possible:
        # then we can do some rounding down logic later
        mid = (left+right) // 2
        mid_squared = mid ** 2

        if mid_squared == x:
            return mid
        elif mid_squared > x:
            right = mid - 1
        else:
            left = mid + 1

    # from the prompt, we are allowed to round down for example, the square root of 8 is 2.82842..., we return 2
    # this means that the first val we find where (val**2 <= x) is the correct result

    # left will always be larger or equal to the sq root because of the logic in the above while loop
    while left ** 2 > x:
        left -= 1
    return left

    # # Also works
    # mid = (left + right) // 2
    # while mid ** 2 > x:
    #     mid -= 1
    # return mid

#       this would have worked if we were rounding up
#       while not right ** 2 >= x:
#           right += 1

#       return right
# 2147395599


# without comments
def mySqrtWC(self, x: int):
    if x < 2:
        return x

    left = 1
    right = x
    while left <= right and left ** 2 <= x:
        mid = (left+right) // 2
        mid_squared = mid ** 2

        if mid_squared == x:
            return mid
        elif mid_squared > x:
            right = mid - 1
        else:
            left = mid + 1

    # Also works
    mid = (left + right) // 2
    while mid ** 2 > x:
        mid -= 1
    return mid

    # while left ** 2 > x:
    #    left -= 1
    # return left
