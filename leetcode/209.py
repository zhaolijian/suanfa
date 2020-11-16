# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
# 如果不存在符合条件的子数组，返回 0。


# 方法1 滑动窗口

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        sum_number = sum(nums)
        if sum_number < s:
            return 0
        # 返回结果长度
        res = len(nums)
        temp = 0
        start = 0
        for i in range(len(nums)):
            temp += nums[i]
            while temp >= s:
                res = min(res, i - start + 1)
                temp -= nums[start]
                start += 1
        return res



class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:
            return 0
        length = len(nums)
        start, end = 0, 0
        number = 0
        res = length + 1
        while end < length:
            number += nums[end]
            while number >= s:
                res = min(res, end - start + 1)
                number -= nums[start]
                start += 1
            end += 1
        return 0 if res == length + 1 else res


# 方法2 二分查找
import bisect
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:
            return 0
        res = float('inf')
        # 前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        if nums[-1] < s:
            return 0
        for i in range(len(nums)):
            if nums[i] >= s:
                index = bisect.bisect_left(nums, nums[i] - s)
                # 数组中有这个数:nums[i] - s
                if nums[i] == nums[index] + s:
                    res = min(res, i - index)
                # 数组中没有这个数,插入的位置为index
                else:
                    res = min(res, i - index + 1)
        return res

