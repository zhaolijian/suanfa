#
class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if length < 2:
            return 0
        prices.insert(0, 0)
        last_last_sell, last_last_hold = 0, 0
        last_sell, last_hold = 0, -prices[1]
        cur_sell, cur_hold = 0, 0
        for i in range(2, length + 1):
            cur_hold = max(last_hold, last_last_sell - prices[i])
            cur_sell = max(last_sell, last_hold + prices[i])
            last_last_hold, last_last_sell = last_hold, last_sell
            last_hold, last_sell = cur_hold, cur_sell
        return cur_sell


# 买卖股票含冷冻期
class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if length < 2:
            return 0
        # 当前卖出股票最大利润,当前拥有股票最大利润,上次卖出股票最大利润
        cash, hold, last_cash = 0, -prices[0], 0
        for i in range(1, length):
            temp = cash
            cash = max(cash, hold + prices[i])
            hold = max(hold, last_cash - prices[i])
            last_cash = temp
        return cash


# 方法2 dp
# 买卖股票含冷冻期
class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if length < 2:
            return 0
        # 每一天的现金最大利润和拥有股票的最大利润
        dp = [[0, 0] for i in range(length + 1)]
        dp[1] = [0, -prices[0]]
        prices.insert(0, 0)
        for i in range(2, length + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[-1][0]


if __name__ == '__main__':
    s = Solution()
    prices = [1,2,3,0,2]
    print(s.maxProfit(prices))