# 方法1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        # 当天处于股票卖出状态利润，当天拥有股票利润
        cash, hold = 0, -prices[0]
        for i in range(1, length):
            cash = max(cash, hold + prices[i])
            hold = max(hold, cash - prices[i])
        return cash


# 方法2 套路dp
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        # 每一个子数组表示当天没有股票最大利润、当天拥有股票最大利润
        dp = [[0, 0] for i in range(length)]
        dp[0] = [0, -prices[0]]
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]

# 方法3，复杂度最低
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        res = 0
        for i in range(1, length):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res