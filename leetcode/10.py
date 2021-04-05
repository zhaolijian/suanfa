class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        row = len(s) + 1
        col = len(p) + 1
        dp=[[False for i in range(col)] for j in range(row)]
        dp[0][0] = True
        for i in range(2, col):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, row):
            for j in range(1, col):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # 题目说了,保证每次出现字符 * 时，前面都匹配到有效的字符,所以不可能p[0]=‘*’
                elif p[j - 1] == '*':
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[-1][-1]







# class Solution(object):
#     def isMatch(self, text, pattern):
#         memo = {}
#         def dp(i, j):
#             if (i, j) not in memo:
#                 # 如果已经遍历到pattern最后一个位置+1，则判断是否遍历到text最后一个位置+1即可
#                 if j == len(pattern):
#                     ans = i == len(text)
#                 else:
#                     # 如果还没遍历完并且pattern的第j个位置与text的第i个位置相等或者为'.'
#                     first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                     # 如果当前位置的下一个位置为*
#                     if j+1 < len(pattern) and pattern[j+1] == '*':
#                         ans = dp(i, j+2) or first_match and dp(i+1, j)
#                     # 如果当前位置的下一个位置不为*
#                     else:
#                         ans = first_match and dp(i+1, j+1)
#                 memo[i, j] = ans
#             return memo[i, j]
#         # 当前遍历text位置、pattern位置
#         return dp(0, 0)


if __name__ == '__main__':
    s = Solution()
    text = "mississippi"
    pattern = "mis*is*p*."
    print(s.isMatch(text, pattern))
