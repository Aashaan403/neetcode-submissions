class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        maxim = minim =0
        profit = 0
        for k in range(size-1):
            minim = prices[k]
            minim = min(prices[k],minim)
            maxim = max(prices[k+1:])
            profit = max(profit,maxim-minim)
        return profit

        