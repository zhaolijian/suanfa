# 动态规划
class Solution:
    # 背包问题
    def findTargetSumWays(self, nums, S: int) -> int:
        length = len(nums)
        sum_number = sum(nums)
        if S > sum_number or S < -sum_number:
            return 0
        dp = [[0 for i in range(2 * sum_number + 1)] for j in range(length)]
        # 当为0的时候前面添正号和负号都可以
        if nums[0] == 0:
            dp[0][sum_number] = 2
        else:
            dp[0][sum_number - nums[0]] = 1
            dp[0][sum_number + nums[0]] = 1
        for i in range(1, length):
            for j in range(2 * sum_number + 1):
                temp1 = j - nums[i] if j - nums[i] >= 0 else 0
                temp2 = j + nums[i] if j + nums[i] <= 2 * sum_number else 0
                # dp[i- 1][0]肯定为0, 只有dp[length - 1][0]才为1
                dp[i][j] = dp[i - 1][temp1] + dp[i - 1][temp2]
        return dp[-1][S + sum_number]

# 方法对，但是复杂度过高
# class Solution:
#     def __init__(self):
#         self.res = 0
#     def findTargetSumWays(self, nums, S: int) -> int:
#         def func(nums, index, length, S):
#             if index >= length:
#                 return
#             elif length - 1 == index:
#                 if nums[index] == 0 and S == 0:
#                     self.res += 2
#                 elif nums[index] == S or nums[index] == -S:
#                     self.res += 1
#             else:
#                 func(nums, index + 1, length, S - nums[index]) or func(nums, index + 1, length, S + nums[index])
#         length = len(nums)
#         func(nums, 0, length, S)
#         return self.res


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1]
    S = 2
    print(s.findTargetSumWays(nums, S))