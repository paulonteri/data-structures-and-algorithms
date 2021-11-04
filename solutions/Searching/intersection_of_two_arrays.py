""" 
Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]
Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.

https://leetcode.com/problems/intersection-of-two-arrays
"""


"""  
Alternative approach: sort the input arrays and use two pointers
"""


class Solution:
    def intersection(self, nums1, nums2):
        result = set()

        one = set(nums1)
        two = set(nums2)

        for num in one:
            if num in one and num in two:
                result.add(num)
        for num in two:
            if num in one and num in two:
                result.add(num)

        return list(result)


class Solution_:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
