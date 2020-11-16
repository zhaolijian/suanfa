# 方法1： 自顶向下
# from functools import lru_cache
#
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#
#         # reframe the problem
#         nums = [1] + nums + [1]
#
#         # cache this
#         @lru_cache(None)
#         def dp(left, right):
#
#             # no more balloons can be added
#             if left + 1 == right: return 0
#
#             # add each balloon on the interval and return the maximum score
#             return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))
#
#         # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
#         return dp(0, len(nums)-1)


# 方法2： 自底向上
class Solution:
    def maxCoins(self, nums) -> int:

        # reframe problem as before
        nums = [1] + nums + [1]
        n = len(nums)

        # dp will store the results of our calls
        dp = [[0] * n for _ in range(n)]

        # iterate over dp and incrementally build up to dp[0][n-1]
        for left in range(n-3, -1, -1):
            for right in range(left+2, n):
                # 思路：对于区间（left, right）,相求这个区间的最大值，遍历这个区间中的元素，对于每一个元素，假设该元素是该开区间最后一个戳破的气球
                # 则获取左区间（left, i）值、右区间值（i， right）和nums[left] * nums[i] * nums[right]。获取最大值
                # same formula to get the best score from (left, right) as before
                dp[left][right] = max(nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left+1, right))

        return dp[0][n-1]


if __name__ == '__main__':
    s = Solution()
    nums = [3,1,5,8]
    print(s.maxCoins(nums))