# 连续子数组的最大和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        temp = 0
        for i in range(len(nums)):
            if temp <= 0:
                res = max(res, nums[i])
                temp = nums[i]
            else:
                res = max(res, temp + nums[i])
                temp += nums[i]
        return res