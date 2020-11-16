# 数据流中的第k大元素
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。假设 nums 的长度≥ k-1 且k ≥ 1。
# heapq（堆）包的使用
from heapq import *


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums
        heapify(self.nums)
        temp = len(nums) - k
        while temp > 0:
            heappop(self.nums)
            temp -= 1

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        else:
            if self.nums[0] < val:
                heapreplace(self.nums, val)
        return self.nums[0]


# from heapq import *
# 创建最小堆  heapify(array)
# 向最小堆中添加元素 heappush(array, value)
# 删除最小堆中的最小元素，并添加新值 heapreplace(array, value)
# 删除并返回最小堆中的最小元素 heappop(array)
# 返回array中最大的n个元素/最小的n个元素（通过堆实现） nlargest(n, array) nsmallest(n, array)


# 创建最大堆 _heapify_max(array)
# 删除最大堆中的最大元素，并添加新值 _heapreplace_max(array, value)
# 删除并返回最大堆中的最大元素 _heappop_max(array)
# 返回array中最大的n个元素/最小的n个元素（通过堆实现） nlargest(n, array) nsmallest(n, array)
# 最大堆中不支持push元素
