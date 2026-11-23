class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        first = 0
        second = 1
        buy = 0
        sell = 0
        while second < (len(prices)):
            if prices[second] - prices[first] > prices[sell] - prices[buy]:
                buy = first
                sell = second
            if prices[second] < prices[first]:
                first = second
            second +=1
        profit = prices[sell]-prices[buy]
        return profit