class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price= prices[0]
        max_profit=0

        for i,n in enumerate(prices):
            if n < min_price:
                min_price =n 
            profit= n - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
            
