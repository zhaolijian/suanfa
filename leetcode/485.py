# 给定一个二进制数组， 计算其中最大连续 1 的个数。
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        res = 0
        cur = 0
        for ele in nums:
            if ele == 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        return res