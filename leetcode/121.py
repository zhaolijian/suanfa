# 一次买卖股票最佳时机，通过记录价格最小值，遍历的每一个值减去最小值，获得最大利润值
class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        res = 0
        min_val = prices[0]
        for ele in prices:
            if ele < min_val:
                min_val = ele
            res = max(res, ele - min_val)
        return res