"""
Reaching Points:

Given four integers sx, sy, tx, and ty, 
    return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.
The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).

Example 1:
    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: true
    Explanation:
        One series of moves that transforms the starting point to the target is:
        (1, 1) -> (1, 2)
        (1, 2) -> (3, 2)
        (3, 2) -> (3, 5)
Example 2:
    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: false
Example 3:
    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: true

https://leetcode.com/problems/reaching-points
"""

"""

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
Given a starting point (sx, sy) and a target point (tx, ty),
 return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty).
 Otherwise, return False.
"""


def canReach(x1, y1, x2, y2):
    if tryReach(x1, y1, x2, y2):
        return "Yes"
    return "No"

# # # stack overflow at canReach(1, 1, 1000, 1000)
# def tryReach(x1, y1, x2, y2):
#     if x1 == x2 and y1 == y2:
#         return True
#     elif x1 > x2 or y1 > y2:
#         return False
#     return tryReach(x1 + y1, y1, x2, y2) or tryReach(x1, y1 + x1, x2, y2)


# optimization
# observation: x1 and x2 must have same GCD (greatest common divisor) as x2 and y2
def tryReach(x, y,  x2,  y2):
    while x2 != 0:
        # y2 - y % x2 are the number of subtractions needed to reach y, if there are 0 subtractions to get to y, then we have found y
        if x2 == x and y2 >= y and (y2 - y) % x2 == 0:
            return True
        else:
            y2 %= x2
            # swap
            x2, y2 = y2, x2
            # original x match original x2
            x, y = y, x
    return False


print("Should be No: ", canReach(1, 2, 2, 1))
print("Should be Yes: ", canReach(1, 4, 5, 9))
print("Should be No: ", canReach(1, 1, 10, 12))
print("Should be No: ", canReach(1, 1, 1000, 1000))
