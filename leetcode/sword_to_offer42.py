# 连续子数组的最大和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        already = 0
        for ele in nums:
            if already <= 0:
                already = ele
            else:
                already += ele
            if already > res:
                res = already
        return res