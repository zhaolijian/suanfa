# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# 字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
# 题目数据保证答案符合 32 位带符号整数范围。

# dp
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        # dp[i][j]表示s[i:]的子序列中t[j:]出现的次数
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        # 如果s[i]==t[j],则dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]
        # 如果s[i]!=t[j],则dp[i][j] = d[i + 1][j]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        # 与上面做法不同的是，dp[i][j]表示s[:i]的子序列中t[:j]出现的次数
        dp = [[0 for i in range(len_t + 1)] for j in range(len_s + 1)]
        for i in range(len_s + 1):
            dp[i][0] = 1
        for i in range(1, len_s + 1):
            for j in range(1, len_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len_s][len_t]


# dfs 超时
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res, len_s, len_t = 0, len(s), len(t)
        if len_t > len_s:
            return 0

        def func(start_s, start_t):
            nonlocal res, len_s, len_t
            if len_t - start_t > len_s - start_s:
                return
            if s[start_s] == t[start_t]:
                if start_t == len_t - 1:
                    res += 1
                else:
                    func(start_s + 1, start_t + 1)
            func(start_s + 1, start_t)

        func(0, 0)
        return res