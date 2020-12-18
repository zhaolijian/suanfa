# 给定一个正整数数组 nums。
# 找出该数组内乘积小于 k 的连续的子数组的个数。

# 双指针
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        number = 1
        res, left = 0, 0
        # 每次统计以right索引所在位置为结束位置的数组个数
        for right, ele in enumerate(nums):
            number *= ele
            while number >= k:
                number //= nums[left]
                left += 1
            res += right - left + 1
        return res


# 累乘--》对数的累加和
from math import log
from bisect import bisect_left
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        k = log(k)
        res = 0
        # 将累乘数组转换为对数的累加和数组
        array = [0, log(nums[0])]
        for i in range(1, len(nums)):
            array.append(array[-1] + log(nums[i]))
        for i, ele in enumerate(nums):
            temp = bisect_left(array, array[i] + k)
            res += temp - i - 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [10,5,2,6]
    # 2 3 2 1
    k = 100
    print(s.numSubarrayProductLessThanK(nums, k))