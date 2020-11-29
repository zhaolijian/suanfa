# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
# 如果数组元素个数小于 2，则返回 0。


# 方法1 桶排序
# 思想： 对于最小值为min_,最大值为max_的数组，相邻元素的最大值一定大于等于width = (max_ - min_) // (length - 1)，所以将数组按照值分桶，桶宽为width
# 相邻元素的最大值一定产生于后一个桶的最小值-前一个桶的最大值
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        max_, min_ = max(nums), min(nums)
        # 桶宽度
        width = max(1, (max_ - min_) // (length - 1))
        # 桶数
        buckets = (max_ - min_) // width + 1
        init = [[] for i in range(buckets)]
        for ele in nums:
            init[(ele - min_) // width].append(ele)
        last_val = float('inf')
        res = 0
        for i in range(buckets):
            if init[i] and last_val != float('inf'):
                res = max(res, min(init[i]) - last_val)
            if init[i]:
                last_val = max(init[i])
        return res