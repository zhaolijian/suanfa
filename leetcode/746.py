# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。


# 方法1
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        length = len(cost)
        dp = [0] * (length + 1)
        for i in range(2, length + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[-1]


# 方法2
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        length = len(cost)
        ll_value, l_value, cur = 0, 0, 0
        for i in range(2, length + 1):
            cur = min(ll_value + cost[i - 2], l_value + cost[i - 1])
            ll_value = l_value
            l_value = cur
        return cur