# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值。


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, length):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        length = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0]] * (length - 1)
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]