# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        index_2, index_3, index_5 = 0, 0, 0
        i = 1
        dp = [1]
        while i < n:
            min_val = min(dp[index_2] * 2, dp[index_3] * 3, dp[index_5] * 5)
            if dp[index_2] * 2 == min_val:
                dp.append(dp[index_2] * 2)
                index_2 += 1
            if dp[index_3] * 3 == min_val:
                if min_val != dp[-1]:
                    dp.append(dp[index_3] * 3)
                index_3 += 1
            if dp[index_5] * 5 == min_val:
                if min_val != dp[-1]:
                    dp.append(dp[index_5] * 5)
                index_5 += 1
            i += 1
        return dp[-1]