# -*- coding:utf-8 -*-
# 连续子数组的最大和


# 动态规划问题
# init[i] = max(init[i-1]+array[i], array[i])
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) <= 1:
            return sum(array)
        init = [0 for i in range(len(array))]
        init[0] = array[0]
        for j in range(1, len(array)):
            init[j] = max(init[j - 1] + array[j], array[j])
        return max(init)
