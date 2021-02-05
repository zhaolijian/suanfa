# 给定一个整数类型的数组 nums，请编写一个能够返回数组 “中心索引” 的方法。
# 我们是这样定义数组 中心索引 的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。


class Solution:
    def pivotIndex(self, nums) -> int:
        if not nums:
            return -1
        sum_number = sum(nums)
        if sum_number == nums[0]:
            return 0
        cur = 0
        for i in range(1, len(nums)):
            cur += nums[i - 1]
            if cur == sum_number - cur - nums[i]:
                return i
        return -1