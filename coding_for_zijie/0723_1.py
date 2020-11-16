# 有很多个无序数（数据没有范围，可正可负，可以非常大），一个个读入，想一个办法在任意时刻，迅速返回以读数字的中位数。
# 比如我读到101个数的时候暂停，需要返回第51大的。读到200的时候暂停，需要返回100和101的平均数。
import heapq
class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        # 小顶堆取相反数就变成大顶堆了
        heapq.heapify(self.max_heap)
        self.flag = 0

    def add(self, val):
        self.flag += 1
        heapq.heappush(self.min_heap, val)
        if self.flag % 2:
            return self.min_heap[0]
        else:
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -temp)
            return (self.min_heap[0] - self.max_heap[0]) / 2


if __name__ == '__main__':
    s = Solution()
    print(s.add(1))
    print(s.add(2))
    print(s.add(3))
    print(s.add(4))
    print(s.add(5))
    print(s.add(6))