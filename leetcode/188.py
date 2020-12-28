# 给定一个整数数组prices，它的第i个元素prices[i]是一支给定的股票在第i天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成k笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution:
    def maxProfit(self, k: int, prices) -> int:
        if not prices:
            return 0
        length = len(prices)
        # 不加k >= length // 2判断也可以执行成功，另外讨论的目的是针对该情况优化复杂度
        if k >= length // 2:   # 退化为不限制交易次数
            profit = 0
            for i in range(1, length):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        # 限制交易次数为k
        res = 0
        # 该方法中完成交易的标志是一次买入一次卖出
        # 天数、交易次数、是否拥有股票
        dp = [[[0 for i in range(2)] for j in range(k + 1)] for n in range(length)]
        # 最后一维0表示没有股票，1表示拥有股票
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        # 第0天的第一次交易---第k次交易都是不可能的
        for i in range(1, k + 1):
            dp[0][i][0] = float('-inf')
            dp[0][i][1] = float('-inf')
        for m in range(1, length):
            # 第m天0次交易,不拥有股票的利润为0
            dp[m][0][0] = 0
            # 第m天0次交易,拥有股票的利润
            dp[m][0][1] = max(dp[m-1][0][1], - prices[m])
            for n in range(1, k + 1):
                dp[m][n][0] = max(dp[m - 1][n][0], dp[m - 1][n - 1][1] + prices[m])
                dp[m][n][1] = max(dp[m - 1][n][1], dp[m - 1][n][0] - prices[m])
        for n in range(k + 1):
            res = max(res, dp[length - 1][n][0])
        return res


if __name__ == '__main__':
    s = Solution()
    k = 2
    prices = [3,2,6,5,0,3]
    print(s.maxProfit(k, prices))