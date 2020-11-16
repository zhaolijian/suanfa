# 通配符匹配
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        dp = [[False for i in range(len_p + 1)] for j in range(len_s + 1)]
        dp[0][0] = True
        for i in range(1, len_p + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]