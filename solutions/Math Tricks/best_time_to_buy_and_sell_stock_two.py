""" 
Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.


Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
        Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
        Total profit is 4 + 3 = 7.
Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
        Total profit is 4.
Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
"""


class Solution:
    def maxProfit(self, prices):
        """
        If we analyze the graph, we notice that the points of interest are the consecutive valleys and peaks.
        Add every upward slope(valley->peak)
        https://www.notion.so/paulonteri/Two-Pointers-78c9f1659ca14bbbadace29a5d252a41#ca35efcb515445a091c0a0dfcefed057
        """
        result = 0

        prev_min = prices[0]
        prev_max = prices[0]
        for idx in range(1, len(prices)):

            if prices[idx] < prev_max:
                # add prev slope we were on
                result += prev_max-prev_min
                # reset slope
                prev_max = prices[idx]
                prev_min = prices[idx]

            else:
                # increase slope
                prev_max = prices[idx]

        # add prev slope we were on
        result += prev_max-prev_min

        return result


""" 

"""


class Solution_:
    def maxProfit(self, prices):
        """
        go on crawling over every slope and 
        keep on adding the profit obtained from every consecutive transaction
        """
        result = 0

        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx-1]:
                result += prices[idx] - prices[idx-1]

        return result
