""" 
Coin Change 2/Total Unique Ways To Make Change:

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
    Input: amount = 5, coins = [1,2,5]
    Output: 4
    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
Example 2:
    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:
    Input: amount = 10, coins = [10]
    Output: 1

https://leetcode.com/problems/coin-change-2/
https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change
"""


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- have a recursive function:
    - for each number in the array, choose to include it:
        - subtract the number from the amount and pass it down the recursive function
        - once you reach 0 return one of less than 0 return 0
    - add up all the results
    
    - cache the total for each amount
    
    - ensure no duplicates by dividing the recursion trees by starting index
        - for examples for coins = [1,2,5]
            - index 0 tree: [1,2,5]
            - index 1 tree: [2,5]
            - index 2 tree: [5]
"""


class Solution0SLOW:  # times out on leetcode
    def changeHelper(self, amount, coins, cache, idx):
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        if (idx, amount) in cache:
            return cache[(idx, amount)]

        total = 0
        for i in range(idx, len(coins)):
            total += self.changeHelper(amount-coins[i], coins, cache, i)

        cache[(idx, amount)] = total
        return cache[(idx, amount)]

    def change(self, amount, coins):
        return self.changeHelper(amount, coins, {}, 0)


class Solution0SLOW2:  # times out on leetcode
    def changeHelper(self, amount, coins, cache, idx):
        if amount == 0:
            return 1
        if amount < 0 or idx == len(coins):
            return 0
        if cache[idx][amount] != False:
            return cache[idx][amount]

        total = 0
        # use it then next time we can decide to leave it out or use it again
        total += self.changeHelper(amount-coins[idx], coins, cache, idx)
        # not use coin and skip to the next
        total += self.changeHelper(amount, coins, cache, idx+1)

        cache[idx][amount] = total
        return cache[idx][amount]

    def change(self, amount, coins):
        cache = [[False for _ in range(amount+1)] for _ in range(len(coins))]
        return self.changeHelper(amount, coins, cache, 0)


class Solution0:
    def changeHelper(self, amount, coins, cache, idx):
        if amount == 0:
            return 1
        if amount < 0 or idx == len(coins):
            return 0
        if (idx, amount) in cache:
            return cache[(idx, amount)]

        total = 0
        # use it then next time we can decide to leave it out or use it again
        total += self.changeHelper(amount-coins[idx], coins, cache, idx)
        # not use coin and skip to the next
        total += self.changeHelper(amount, coins, cache, idx+1)

        cache[(idx, amount)] = total
        return cache[(idx, amount)]

    def change(self, amount, coins):
        return self.changeHelper(amount, coins, {}, 0)


""" 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# if amount is zero you can always make that change with zero/no coins
# if there are no coins there is no way to make change for amounts greater than zero

number of ways = (
    using the coin     => reduce the amount by the coin's value (move left by the coin's value)
+   not using the coin => remove the coin (move up by one)
)

        0  1  2  3  4  5
[]      1  0  0  0  0  0
[1]     1  1  1  1  1  1
[1,2]   1
[1,2,5] 1

"""


class Solution:

    def change(self, amount, coins):
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins)+1)]

        # Fill in defaults
        # if amount is zero you can always make that change with zero/no coins
        for i in range(len(coins)+1):
            dp[i][0] = 1
        # if there are no coins there is no way to make change for amounts greater than zero
        for i in range(1, amount+1):
            dp[0][i] = 0

        for coin in range(1, len(coins)+1):
            for amount in range(1, amount+1):
                actual_coin = coins[coin-1]
                total = 0

                # not use coin => remove the coin (move up by one)
                total += dp[coin-1][amount]
                # use coin => reduce the amount by the coin's value (move left by the coin's value)
                if actual_coin <= amount:
                    total += dp[coin][amount-actual_coin]

                # print(coin,actual_coin,amount,total)
                dp[coin][amount] = total

        return dp[-1][-1]


# only keep needed fields in memory
class Solution_:

    def change(self, amount, coins):
        dp = [0 for _ in range(amount+1)]
        # if amount is zero you can always make that change with zero/no coins
        dp[0] = 1

        for coin in coins:
            for amount in range(1, amount+1):
                total = dp[amount]  # (ways_for_prev_coin) coin not added

                if coin <= amount:
                    total += dp[amount-coin]  # coin added

                dp[amount] = total

        return dp[-1]


# -----------------------------------------------

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    denoms.sort()
    return helper(n, denoms)


def helper(n, denoms):

    array = list(range(1, n+1))

    for idx in range(len(array)):
        times = 0
        for denom in denoms:
            if denom <= idx:
                times += 1
            else:
                break
        array[idx] = times
