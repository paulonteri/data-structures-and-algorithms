"""
Coin Change:

You are given an integer array coins representing coins of different denominations and 
 an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
Example 2:

    Input: coins = [2], amount = 3
    Output: -1
Example 3:

    Input: coins = [1], amount = 0
    Output: 0
Example 4:

    Input: coins = [1], amount = 1
    Output: 1
Example 5:

    Input: coins = [1], amount = 2
    Output: 2

https://leetcode.com/problems/coin-change/

"""
""" 
Min Number Of Coins For Change:

Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money, 
write a function that returns the smallest number of coins needed to make change for (to sum up to) that target amount using the given coin denominations.
Note that you have access to an unlimited amount of coins. 
    In other words, if the denominations are [1, 5, 10], you have access to an unlimited amount of 1s, 5s, and 10s.
If it's impossible to make change for the target amount, return -1.

https://www.algoexpert.io/questions/Min%20Number%20Of%20Coins%20For%20Change
"""


class SolutionMEM:
    def coinChange(self, coins, amount):

        cache = [[False for _ in range(amount+1)] for _ in range(len(coins))]
        res = self.coinChangeHelper(coins, 0, amount, cache)
        if res == float('inf'):
            return -1
        return res

    def coinChangeHelper(self, coins, idx, amount, cache):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if idx == len(coins):
            return float('inf')

        if cache[idx][amount]:
            return cache[idx][amount]

        # use it then next time we can decide to leave it out or use it again
        used = 1 + self.coinChangeHelper(coins, idx, amount-coins[idx], cache)

        # not use coin and skip to the next
        not_used = self.coinChangeHelper(coins, idx+1, amount, cache)

        cache[idx][amount] = min(used, not_used)

        return cache[idx][amount]


"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

i = infinity
         0 1 2 3 4 5 6 7 8 9 10 11
[]       0 i i i i i i i i i i  i
[1]      0 1 2 3 4 5 6 7 8 9 10 11
[1,2]    0 1 1 2 2 3 3 4 4 5 5  6
[1,2,5]  0 1 1 2 2 1 2 2 3 4 2  3

"""


class SolutionDP:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1

        dp = [
            [float('inf') for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 0

        for coin in range(1, len(coins)+1):
            for amount in range(1, amount+1):
                coin_val = coins[coin-1]

                not_use = dp[coin-1][amount]
                use = float('inf')
                if coin_val <= amount:
                    use = 1 + dp[coin][amount-coin_val]

                dp[coin][amount] = min(use, not_use)

        if dp[-1][-1] == float('inf'):
            return -1
        return dp[-1][-1]


class SolutionDPImproved:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1

        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for amount in range(1, amount+1):
            for coin in coins:
                if coin > amount:
                    continue
                use = 1 + dp[amount-coin]
                dp[amount] = min(use, dp[amount])

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
