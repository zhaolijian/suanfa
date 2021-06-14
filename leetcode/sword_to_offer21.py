# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length < 2:
            return nums
        left, right = 0, length - 1
        while left < right:
            # 从左往右找到第一个偶数
            while left < right and nums[left] % 2 == 1:
                left += 1
            # 从右往左找到第一个奇数
            while left < right and nums[right] % 2 == 0:
                right -= 1
            # 交换位置
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums