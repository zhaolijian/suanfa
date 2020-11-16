# 判断子序列
# 方法1 双指针
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


# 方法2 dp
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]

        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1
        return True


# dp
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n == 0:
            return True
        if m == 0:
            return False
        dp = [[False for i in range(n)] for j in range(m)]
        dp[0][0] = True if t[0] == s[0] else False
        for i in range(1, m):
            if t[i] == s[0]:
                dp[i][0] = True
            else:
                dp[i][0] = dp[i - 1][0]
        for p in range(m):
            for q in range(1, n):
                if t[p] == s[q]:
                    dp[p][q] = dp[p - 1][q - 1]
                else:
                    dp[p][q] = dp[p - 1][q]
        return dp[-1][-1]

if __name__ == '__main__':
    S = Solution()
    s, t = "abc", "ahbgdc"
    print(S.isSubsequence(s, t))
