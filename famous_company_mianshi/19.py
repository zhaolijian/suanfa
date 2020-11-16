# 假设你有一个数组，其中第\ i i 个元素是股票在第\ i i 天的价格。
# 你有一次买入和卖出的机会。（只有买入了股票以后才能卖出）。请你设计一个算法来计算可以获得的最大收益。
class Solution:
    def maxProfit(self , prices ):
        length = len(prices)
        if length <= 1:
            return 0
        res = 0
        min_val = prices[0]
        for i in range(1, length):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                res = max(res, prices[i] - min_val)
        return res