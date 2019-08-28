#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for curr_price in prices[1:]:
            if curr_price < min_price:
                min_price = curr_price
            else:
                max_profit = max(max_profit, curr_price - min_price)

        return max_profit
