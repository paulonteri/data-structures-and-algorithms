"""
Non-Constructible Change:

Given an array of positive integers representing the values of coins in your possession, 
 write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create.
The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).
For example, if you're given
    coins = [1, 2, 5] , 
    the minimum amount of change that you can't create is 4
    If you're given no coins, the minimum amount of change that you can't create is 1

https://www.algoexpert.io/questions/Non-Constructible%20Change
"""

"""  

start at idx 0
coins = [5, 7, 1, 1, 2, 3, 22]
coins = [1, 1, 2, 3, 5, 7, 22]
curr,creatable,non-constructible
1,  1,[]
1,  2,[]
2,  4,[]
3,  7,[]
5, 12,[]
7, 19,[]
22,41,[20,21]

coins = [1, 1, 5]
curr,creatable,non-constructible
1,1,[]
1,2,[]
5,7,[3,4]

coins = [1, 1, 3]
curr,creatable,non-constructible
1,1,[]
1,2,[]
3,5,[]
 , ,[4]

- keep on checking if we can make the prev-constructible + 1
    - if not, return prev-constructible + 1
"""


# 0(nlog(n)) time | 0(1) space
def nonConstructibleChange(coins):
    coins.sort()

    creatable = 0
    for coin in coins:
        # if C > C+1, we cannot make C+1
        if coin > creatable + 1:
            return creatable + 1
        creatable += coin

    return creatable + 1
