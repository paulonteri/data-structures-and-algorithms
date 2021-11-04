"""
Best Time to Buy and Sell Stock: (do Container With Most Water first)

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
 design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, prices):
        min_price_so_far, max_profit = float('inf'), 0

        for price in prices:
            profit = price - min_price_so_far
            max_profit = max(max_profit, profit)

            min_price_so_far = min(min_price_so_far, price)

        return max_profit


""" 

"""


class Solution_:

    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0

        left = 0
        right = 1
        max_profit = 0
        # we need to find the smallest valley following the largest peak -> try to continue increasing the slope
        while right < len(prices):
            max_profit = max(max_profit,  prices[right] - prices[left])

            # try out all values that are larger than left b4 we get a smaller value left
            # increase slope length
            if prices[right] > prices[left] or right == left:
                right += 1

            # # if we find a point that is equal or lower than left (if lower we might make more profit)
            # reset slope
            else:
                left = right  # move left to the smaller value
                right += 1

        return max_profit
