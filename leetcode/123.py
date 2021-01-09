# 方法1
class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        # 天数*交易次数*[无股票，有股票]
        dp = [[[0, 0] for i in range(3)] for j in range(length)]
        dp[0][0], dp[0][1], dp[0][2] = [0, -prices[0]], [float('-inf'), float('-inf')], [float('-inf'), float('-inf')]
        for i in range(1, length):
            dp[i][0] = [0, max(dp[i - 1][0][1], -prices[i])]
            dp[i][1] = [max(dp[i - 1][1][0], dp[i - 1][0][1] + prices[i]),
                        max(dp[i - 1][1][1], dp[i - 1][1][0] - prices[i])]
            dp[i][2] = [max(dp[i - 1][2][0], dp[i - 1][1][1] + prices[i]),
                        max(dp[i - 1][2][1], dp[i - 1][2][0] - prices[i])]
        return max(dp[-1][0][0], dp[-1][1][0], dp[-1][2][0])


# 方法2
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        length = len(prices)
        # 该方法中完成交易的标志是一次买入一次卖出
        # 天数、是否拥有股票、交易次数
        dp = [[[0 for i in range(3)] for j in range(2)] for k in range(length)]
        dp[0][0][0] = 0
        # 下面两种不可能事件
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        dp[0][1][0] = -prices[0]
        # 下面两种不可能事件
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')
        for m in range(1, length):
            dp[m][0][0] = 0
            dp[m][0][1] = max(dp[m - 1][0][1], dp[m - 1][1][0] + prices[m])
            dp[m][0][2] = max(dp[m - 1][0][2], dp[m - 1][1][1] + prices[m])
            dp[m][1][0] = max(dp[m - 1][1][0], dp[m - 1][0][0] - prices[m])
            dp[m][1][1] = max(dp[m - 1][1][1], dp[m - 1][0][1] - prices[m])
            dp[m][1][2] = max(dp[m - 1][1][2], dp[m - 1][0][2] - prices[m])
        return max(dp[length - 1][0][0], dp[length - 1][0][1], dp[length - 1][0][2])


if __name__ == '__main__':
    s = Solution()
    prices = [1, 2, 3, 4, 5]
    print(s.maxProfit(prices))