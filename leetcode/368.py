# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        length = len(nums)
        max_length = 1
        max_val = -1
        # 以i所在位置为最后一个元素的最长有效解子集长度
        dp = [1] * length
        for i in range(length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_length:
                max_length = dp[i]
                max_val = nums[i]
        if max_length == 1:
            return [nums[0]]
        res = []
        # 倒推获取结果集合
        for i in range(length - 1, -1, -1):
            if dp[i] == max_length and max_val % nums[i] == 0:
                res.append(nums[i])
                max_val = nums[i]
                max_length -= 1
            if max_length <= 0:
                break
        return res[::-1]