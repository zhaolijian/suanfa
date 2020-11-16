# 最小路径和
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        dp = [[0 for i in range(w)] for j in range(h)]
        dp[0][0] = grid[0][0]
        for i in range(1, h):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, w):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, h):
            for j in range(1, w):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


# 不知道哪个题了，写到64
# class Solution:
#     def __init__(self):
#         self.res = 0
#
#     def sumNums(self, n: int) -> int:
#         # 短路原则,如果不满足n>1,则不执行self.sumNums(n - 1)
#         n > 1 and self.sumNums(n - 1)
#         self.res += n
#         return self.res
#
# if __name__ == '__main__':
#     s = Solution()
#     n = 4
#     print(s.sumNums(n))