""" 
Friends Of Appropriate Ages

There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.
A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:
    age[y] <= 0.5 * age[x] + 7
    age[y] > age[x]
    age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.
Note that if x sends a request to y, y will not necessarily send a request to x. 
Also, a person will not send a friend request to themself.
Return the total number of friend requests made.

Example 1:
    Input: ages = [16,16]
    Output: 2
    Explanation: 2 people friend request each other.
Example 2:
    Input: ages = [16,17,18]
    Output: 2
    Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:
    Input: ages = [20,30,100,110,120]
    Output: 3
    Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

https://leetcode.com/problems/friends-of-appropriate-ages
"""


""" 
1 <= ages[i] <= 120

x Can send to y if:
    age[y] > 0.5 * age[x] + 7
    age[y] <= age[x]

"abzbvcgdjcsfvvrbzbssvcgdjcsfbzbvsfcgdjc"
"""




from typing import List
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]):
        requests_sent = 0

        age_count = Counter(ages)
        for user_age in ages:
            for stranger_age in age_count:

                if not(stranger_age > 0.5*user_age+7 and stranger_age <= user_age):
                    continue

                stanger_count = age_count[stranger_age]

                if stranger_age == user_age:
                    stanger_count -= 1  # subtract user

                requests_sent += stanger_count

        return requests_sent
