# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
# 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums) -> int:
        d = defaultdict(list)
        for i, ele in enumerate(nums):
            d[ele].append(i)
        # 最短连续子数组长度
        res = float('inf')
        max_len = 0
        for key in d.keys():
            cur_len = len(d[key])
            if cur_len > max_len:
                max_len = cur_len
                res = d[key][-1] - d[key][0] + 1
            elif cur_len == max_len and d[key][-1] - d[key][0] + 1 < res:
                res = d[key][-1] - d[key][0] + 1
        return res
