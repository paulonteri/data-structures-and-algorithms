""" 
Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2, 2]
Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.
3:
[4,9,5]
[9,4,9,8,4]
=> [4,9]

https://leetcode.com/problems/intersection-of-two-arrays-ii
"""


""" 
Alternative: use hashmap/collections.Counter
"""


class Solution:
    def intersect(self, nums1, nums2):
        result = []

        nums1.sort()
        nums2.sort()

        one, two = 0, 0
        while one < len(nums1) and two < len(nums2):
            if nums1[one] == nums2[two]:
                result.append(nums1[one])
                one += 1
                two += 1
            elif nums1[one] < nums2[two]:
                one += 1
            else:
                two += 1
        return result
