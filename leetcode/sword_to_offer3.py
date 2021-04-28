# 找出数组中重复的数字。
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

# 方法1 原地操作
class Solution:
    def findRepeatNumber(self, nums) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]



# 方法2 哈希表
class Solution:
    def findRepeatNumber(self, nums) -> int:
        s = set()
        for ele in nums:
            if ele in s:
                return ele
            s.add(ele)