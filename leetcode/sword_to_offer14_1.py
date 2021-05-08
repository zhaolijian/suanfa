# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。


# 方法1 贪心法
# 经过数学推导，当n<4时，返回n-1,当n=4时，分为2、2，返回4，当n>4时，尽可能的分为长度为3的段
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        if n == 4:
            return n
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n


# 方法2 dp
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[-1]