"""
Merge Sorted Array:
simpler version of Merge K Sorted Lists

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Constraints:
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1.length == m + n
    nums2.length == n
    
https://leetcode.com/problems/merge-sorted-array/
"""


# O(n) time | O(1) space
class Solution:
    def merge(self, nums1, m, nums2, n):

        one = m - 1
        two = n - 1

        # iterate through all the characters in nums1
        for i in reversed(range(m+n)):

            if two < 0:
                return

            # we have to deal with the case where the one pointer goes outside nums1 (-1,-2,...) because
            # many/all of it's values were greater than the ones in nums2
            if nums1[one] < nums2[two] or one < 0:
                nums1[i] = nums2[two]
                two -= 1
            else:
                nums1[i] = nums1[one]
                one -= 1


class Solution0:
    def merge(self, nums1, m, nums2, n):

        one = m - 1
        two = n - 1
        # fill nums1 backwards
        for idx in reversed(range(len(nums1))):

            # handle edge cases
            if two < 0:
                nums1[idx] = nums1[one]
                one -= 1
            elif one < 0:
                nums1[idx] = nums2[two]
                two -= 1

            # fill bey checking which is larger
            elif nums1[one] > nums2[two]:
                nums1[idx] = nums1[one]
                one -= 1
            else:
                nums1[idx] = nums2[two]
                two -= 1


"""
Example:
    Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]
"""
