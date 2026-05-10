class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        max_profit = 0

        for i, p in enumerate(prices):
            if min_buy > p:
                min_buy = p
            else:
                max_profit = max(max_profit, p - min_buy)
        
        return max_profit