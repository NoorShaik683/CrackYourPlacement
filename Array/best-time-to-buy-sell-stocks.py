class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices== sorted(prices, reverse=True):
            return 0
        profit=0
        buy = prices[0]
        for i in prices[1::]:
            if i>buy:
                profit = max(profit, i-buy)
            else:
                buy=i
        return profit
