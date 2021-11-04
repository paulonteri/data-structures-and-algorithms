"""
First Bad Version:

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

Example 2:
    Input: n = 1, bad = 1
    Output: 1

https://leetcode.com/problems/first-bad-version/
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
def isBadVersion(mid):
    pass


class Solution:
    def firstBadVersion(self, n):

        left = 1
        right = n
        while left < right:
            mid = (left+right) // 2

            if isBadVersion(mid):
                # in the next loop, this will result in left being brought closer to the bad versions
                # [1,2,3] if bv=2, l=0, r=2, in the next, l=2

                # avoid skipping bad versions
                right = mid
            else:
                # only move left if mid version is good
                # this ensures left never skips any bad version, it will always land on the first bad version
                # skip all good versions
                left = mid + 1

        return left


"""
try to move left to the first bad version - make sure not to pass it (bad version) with right

"""
"""
// [1,2,3]

[0,1,2,3,4,5,6,7,8]
[1,2,3,4,5,6,7,8,9]
6 and above

r = 9
l = 1
m = 5

r = 9
l = 6
m = 7




[0,1,2,3,4,5,6,7,8]
[1,2,3,4,5,6,7,8,9]
2 and above

r = 9
l = 1
m = 5

r = 5
l = 1
m = 2

r = 2
l = 1
m = 1

r = 2
l = 2
m = 2
break

"""


class Solution00:
    def firstBadVersion(self, n):

        left = 1
        right = n

        while left < right:

            mid = (left+right) // 2

            # only move left if mid version is good
            # this ensures left never skips any bad version, it will always land on the first bad version
            if not isBadVersion(mid):
                left = mid + 1

            # try and move right closer and closer to the first bad version
            else:
                right = mid

        return left
