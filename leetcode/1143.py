# 最长公共子序列
# 动态规划
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0 for i in range(len2)] for j in range(len1)]
        for i in range(len1):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(len2):
            if text1[0] == text2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, len1):
            for j in range(1, len2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    text1, text2 = "abcde", "ace"
    print(s.longestCommonSubsequence(text1, text2))