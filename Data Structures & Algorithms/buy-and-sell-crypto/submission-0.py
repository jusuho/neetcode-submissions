class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, p in enumerate(prices):
            if i == len(prices) - 1:
                return max_profit
            max_profit = max(max_profit, max(prices[i+1:]) - p )