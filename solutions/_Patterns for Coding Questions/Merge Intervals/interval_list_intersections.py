"""
Interval List Intersections:

You are given two lists of closed intervals, firstList and secondList, 
    where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 
For example, the intersection of [1, 3] and [2, 4] is [2, 3].


Example:
    Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
    Output: [2, 3], [5, 6], [7, 7]
    Explanation: The output list contains the common intervals between the two lists.
Example:
    Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
    Output: [5, 7], [9, 10]
    Explanation: The output list contains the common intervals between the two lists.
Example 1:
    Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:
    Input: firstList = [[1,3],[5,9]], secondList = []
    Output: []
Example 3:
    Input: firstList = [], secondList = [[4,8],[10,12]]
    Output: []
Example 4:
    Input: firstList = [[1,7]], secondList = [[3,10]]
    Output: [[3,7]]

https://leetcode.com/problems/interval-list-intersections/
https://www.educative.io/courses/grokking-the-coding-interview/JExVVqRAN9D
"""

"""
Solution:

---

# Note: Each list of intervals is pairwise disjoint and in sorted order.

- check if start of two <= end of one and end of two >= start of one (are not before or after each other)
- if so:
    intersection = [max(start_one, start_two), min(end_one, end_two)]
        - futhest start, first end (end that is in both intervals)
- move the pointer of the interval with the least ending forward
    - list with the smaller might have another intersection in the current bigger intersection
    - because the bigger one might still be in another intersection

firstList =  [[0,2],[5,10],[13,23],[24,25]], 
secondList = [[1,5],[8,12],[15,24],[25,26]]

one,two,res
0,0,[] => intersection = [max(0,1), min(2,5)]
1,0,[[1,2], ] => intersection = [max(5,1), min(10,5)]
1,1,[[1,2],[5,5] ] => intersection = [max(5,8), min(10,12)]
2,1,[[1,2],[5,5],[8,10] ] => intersection = None
2,2,[[1,2],[5,5],[8,10] ] => intersection = [max(13,15), min(23,24)]
3,2,[[1,2],[5,5],[8,10],[15,23] ] => intersection = [max(24,15), min(25,24)]
3,3,[[1,2],[5,5],[8,10],[15,23],[24,24] ] => intersection = [max(24,25), min(25,26)]
3,3,[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25] ]

"""

# O(n+m) time | O(n+m) space -> where n and m are the lengths of the two lists


class Solution:
    def getIntersection(self, l_one, l_two):
        # futhest start, first end -> ensures interval is in both intervals
        return [max(l_one[0], l_two[0]), min(l_one[1], l_two[1])]

    def intervalIntersection(self, firstList, secondList):
        if not firstList or not secondList:
            return []

        res = []
        one = 0
        two = 0
        while one <= len(firstList)-1 and two <= len(secondList)-1:
            l_one = firstList[one]
            l_two = secondList[two]

            if l_two[0] <= l_one[1] and l_two[1] >= l_one[0]:  # if has interval
                res.append(self.getIntersection(l_one, l_two))

            # move forward the pointer of list with the least ending
            #   so that we can continue evaluating the one with the furthest end in the next loop
            if two == len(secondList)-1 or l_one[1] < l_two[1]:
                one += 1
            else:
                two += 1

        return res
