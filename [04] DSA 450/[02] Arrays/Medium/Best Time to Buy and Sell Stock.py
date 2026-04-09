# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        buy, profit = 0, 0
        for i in range(1, n):
            if prices[i] < prices[buy]:
                buy = i
            else:
                temp = prices[i] - prices[buy]
                if profit < temp:
                    profit = temp
        return profit