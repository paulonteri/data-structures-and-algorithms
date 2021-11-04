""" 
Angle Between Hands of a Clock

Given two numbers, hour and minutes. 
Return the smaller angle (in degrees) formed between the hour and the minute hand.

Example 1:
    Input: hour = 12, minutes = 30
    Output: 165
Example 2:
    Input: hour = 3, minutes = 30
    Output: 75
Example 3:
    Input: hour = 3, minutes = 15
    Output: 7.5
Example 4:
    Input: hour = 4, minutes = 50
    Output: 155
Example 5:
    Input: hour = 12, minutes = 0
    Output: 0

https://leetcode.com/problems/angle-between-hands-of-a-clock
"""


class Solution:
    def angleClock(self, hour: int, minutes: int):
        """ 
        - calculate hour degree
            (hour/12 * 360) + (minute/60 * 30)
        - calculate minute degree
            - minute/60 * 360
        """
        hours = hour
        if hour == 12:
            hours = 0

        hours_degree = (360 * hours/12) + (30 * minutes/60)
        minutes_degree = 360 * minutes/60

        diff = abs(hours_degree-minutes_degree)
        return min(diff, abs(360-diff))
