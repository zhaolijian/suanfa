# 方法1 dp
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    n = 8
    print(s.integerBreak(n))