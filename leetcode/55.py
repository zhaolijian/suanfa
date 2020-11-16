# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 1:
            return True
        max_loc = nums[0]
        for i in range(1, length):
            if i > max_loc:
                return False
            if i + nums[i] > max_loc:
                max_loc = i + nums[i]
            if max_loc >= length - 1:
                return True
        return False
