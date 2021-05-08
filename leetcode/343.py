# 方法1 dp
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


# 方法2 贪心
# 经过数学推导，当n<4时，返回n-1,当n=4时，分为2、2，返回4，当n>4时，尽可能的分为长度为3的段
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n == 4:
            return 4
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n


if __name__ == '__main__':
    s = Solution()
    n = 8
    print(s.integerBreak(n))