# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
# 返回符合要求的 最少分割次数 。
class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        dp = [[True for i in range(length)] for j in range(length)]
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = dp[i + 1][j - 1] & (s[i] == s[j])
        res = [float('inf')] * length
        for i in range(length):
            if dp[0][i]:
                res[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        res[i] = min(res[i], res[j] + 1)
        return res[-1]


if __name__ == '__main__':
    s = Solution()
    ss = "aab"
    print(s.minCut(ss))