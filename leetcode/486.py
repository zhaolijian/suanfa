# 给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，
# 然后玩家 1 拿，…… 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。
# 给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

# 二维动态规划
# dp[i][j]为从i到j位置的先选的人和后选的人的最大差，先选的人和后选的人是不固定的
class Solution:
    def PredictTheWinner(self, nums) -> bool:
        length = len(nums)
        dp = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            dp[i][i] = nums[i]
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        # 如果dp[0][length - 1] >= 0说明先选的人会赢，否则会输
        return dp[0][length - 1] >= 0


# 一维动态规划
class Solution:
    def PredictTheWinner(self, nums) -> bool:
        length = len(nums)
        dp = [ele for ele in nums]
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[-1] >= 0

# 记忆化递归
class Solution:
    def PredictTheWinner(self, nums) -> bool:
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == j:
                memo[(i, j)] = nums[i]
                return nums[i]
            temp = max(nums[i] - helper(i + 1, j), nums[j] - helper(i, j - 1))
            memo[(i, j)] = temp
            return temp

        memo = {}
        return helper(0, len(nums) - 1) >= 0


# 递归
class Solution:
    def PredictTheWinner(self, nums) -> bool:
        def helper(i, j):
            if i == j:
                return nums[i]
            return max(nums[i] - helper(i + 1, j), nums[j] - helper(i, j - 1))

        return helper(0, len(nums) - 1) >= 0