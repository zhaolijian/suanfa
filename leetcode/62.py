# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？


# 方法1 dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

# 方法2 组合数学
# 从左上角到右下角的过程中，需要移动 m+n-2次，其中有 m-1 次向下移动，n-1次向右移动。
# 因此路径的总数，就等于从 m+n-2 次移动中选择 m-1次向下移动的方案数，即组合数：
# C m+n−2(下) m−1(上) = (m+n-2)! // ((m-1)! * (n-1)!)
from scipy.special import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)