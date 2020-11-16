class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)
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
            dp[m][0][1] = max(dp[m-1][0][1], dp[m - 1][0][0] - prices[m])
            for n in range(1, k + 1):
                dp[m][n][0] = max(dp[m - 1][n][0], dp[m - 1][n - 1][1] + prices[m])
                dp[m][n][1] = max(dp[m - 1][n][1], dp[m - 1][n][0] - prices[m])
        for n in range(k + 1):
            res = max(res, dp[length - 1][n][0])
        return res