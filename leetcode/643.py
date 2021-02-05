# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        res = sum(nums[:k])
        cur = res
        left, right = 0, k
        while right < len(nums):
            cur += nums[right]
            cur -= nums[left]
            if cur > res:
                res = cur
            right += 1
            left += 1
        return res / k