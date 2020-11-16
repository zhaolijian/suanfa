class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        if length < 2:
            return 0
        else:
            # 不持有股票时的最大收益
            cash = 0
            # 持有股票时的最大收益
            hold = -prices[0]
            for i in range(1, length):
                cash = max(cash, hold + prices[i] - fee)
                hold = max(hold, cash - prices[i])
            return cash