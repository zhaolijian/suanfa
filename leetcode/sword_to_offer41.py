# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
# 例如，
# [2,3,4] 的中位数是 3
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 设计一个支持以下两种操作的数据结构：
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。


from heapq import heapify, heappush, heappushpop, _heapify_max


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        heapify(self.min_heap)
        self.max_heap = []
        heapify(self.max_heap)
        # 数据总数是否为奇数
        self.flag = False

    def addNum(self, num: int) -> None:
        self.flag = True if not self.flag else False
        # 个数为奇数
        if self.flag:
            temp = heappushpop(self.max_heap, -num)
            heappush(self.min_heap, -temp)
        else:
            temp = heappushpop(self.min_heap, num)
            heappush(self.max_heap, -temp)

    def findMedian(self) -> float:
        # 奇数的话从取最小堆堆顶
        if self.flag:
            return self.min_heap[0]
        # 偶数的话取两堆堆顶平均值
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2