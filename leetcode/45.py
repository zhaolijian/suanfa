# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。


class Solution:
    def jump(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return 0
        dp = [float('inf')] * (length)
        dp[0] = 0
        for i in range(length):
            for j in range(i + 1, min(length, i + nums[i] + 1)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]
