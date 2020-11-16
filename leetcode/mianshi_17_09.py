# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。
# 例如，前几个数按顺序应该是 1，3，5，7，9，15，21。


# 某一个素数一定是其他素数的3倍/5倍/7倍
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        n3, n5, n7 = 0, 0, 0
        dp = [0 for i in range(k)]
        dp[0] = 1
        for i in range(1, k):
            dp[i] = min(dp[n3] * 3, dp[n5] * 5, dp[n7] * 7)
            if dp[i] == dp[n3] * 3:
                n3 += 1
            if dp[i] == dp[n5] * 5:
                n5 += 1
            if dp[i] == dp[n7] * 7:
                n7 += 1
        return dp[-1]