# 给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
# 实现 NumArray 类：
# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.sum_array = []
        if nums:
            self.sum_array.append(nums[0])
        for i in range(1, len(nums)):
            self.sum_array.append(self.sum_array[-1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_array[j] - self.sum_array[i - 1] if i > 0 else self.sum_array[j]


if __name__ == '__main__':
    s = NumArray([-2,0,3,-5,2,-1])
    print(s.sumRange(0, 2))
    print(s.sumRange(2, 5))
    print(s.sumRange(0, 5))