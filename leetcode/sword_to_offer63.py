# 只买卖一次股票，只要记录并更新价格最小值即可
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        res = 0
        min_val = prices[0]
        for i in range(1, length):
            res = max(res, prices[i] - min_val)
            min_val = min(min_val, prices[i])
        return res


if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))