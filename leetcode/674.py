# 最长连续递增序列
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += 1
                res = max(res, temp)
            else:
                temp = 1
        return res