# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。
# 结果可能很大，你需要对结果模1000000007。
class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        dp = [1, 1, 2, 4]
        for i in range(4, n + 1):
            dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007)
        return dp[-1]
