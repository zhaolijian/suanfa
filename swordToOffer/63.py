# 因为没有上下限的限制，所以采用大顶堆+小顶堆的形式
# 如果要是有上下限限制，而且范围较小，可以采用桶排序的方式


# class Solution:
#     def __init__(self):
#         self.minNums = []
#         self.maxNums = []
#
#     def maxHeapInsert(self, num):
#         self.maxNums.append(num)
#         lens = len(self.maxNums)
#         i = lens - 1
#         while i > 0:
#             if self.maxNums[i] > self.maxNums[(i - 1) // 2]:
#                 self.maxNums[i], self.maxNums[(i - 1) // 2] = self.maxNums[(i - 1) // 2], self.maxNums[i]
#                 i = （i- 1）// 2
#             else:
#                 break
#
#     def maxHeapPop(self):
#         t = self.maxNums[0]
#         self.maxNums[0] = self.maxNums[-1]
#         self.maxNums.pop()
#         lens = len(self.maxNums)
#         i = 0
#         while 2 * i + 1 < lens:
#             nexti = 2 * i + 1
#             if nexti + 1 < lens and self.maxNums[nexti + 1] > self.maxNums[nexti]:
#                 nexti += 1
#             if self.maxNums[nexti] > self.maxNums[i]:
#                 self.maxNums[i], self.maxNums[nexti] = self.maxNums[nexti], self.maxNums[i]
#                 i = nexti
#             else:
#                 break
#         return t
#
#     def minHeapInsert(self, num):
#         self.minNums.append(num)
#         lens = len(self.minNums)
#         i = lens - 1
#         while i > 0:
#             if self.minNums[i] < self.minNums[(i - 1) // 2]:
#                 self.minNums[i], self.minNums[(i - 1) // 2] = self.minNums[(i - 1) // 2], self.minNums[i]
#                 i = (i - 1) // 2
#             else:
#                 break
#
#     def minHeapPop(self):
#         t = self.minNums[0]
#         self.minNums[0] = self.minNums[-1]
#         self.minNums.pop()
#         lens = len(self.minNums)
#         i = 0
#         while i * 2 + 1 < lens:
#             nexti = 2 * i + 1
#             if nexti + 1 < lens and self.minNums[nexti + 1] < self.minNums[nexti]:
#                 nexti += 1
#             if self.minNums[nexti] < self.minNums[i]:
#                 self.minNums[nexti], self.minNums[i] = self.minNums[i], self.minNums[nexti]
#                 i = nexti
#             else:
#                 break
#         return t
#
#     def Insert(self, num):
#         # 每次向大顶推或小顶堆中添加一个元素
#         if (len(self.minNums) + len(self.maxNums)) % 2 == 0:
#             # 当数目为偶数的时候，将这个值插入大顶堆中，再将大顶堆中根节点（即最大值）插入到小顶堆中；
#             if len(self.maxNums) > 0 and num < self.maxNums[0]:
#                 self.maxHeapInsert(num)
#                 num = self.maxHeapPop()
#             self.minHeapInsert(num)
#         else:
#             # 当数目为奇数的时候，将这个值插入小顶堆中，再将小顶堆中根节点（即最小值）插入到大顶堆中；
#             if len(self.minNums) > 0 and num > self.minNums[0]:
#                 self.minHeapInsert(num)
#                 num = self.minHeapPop()
#             self.maxHeapInsert(num)
#
#     def GetMedian(self):
#         allLen = len(self.minNums) + len(self.maxNums)
#         if allLen == 0:
#             return -1
#         elif allLen % 2 == 1:
#             return self.minNums[0]
#         else:
#             return (self.maxNums[0] + self.minNums[0]) / 2



class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    def maxHeapInsert(self, number):
        self.maxHeap.append(number)
        length = len(self.maxHeap)
        temp = length - 1
        while (temp - 1) // 2 >= 0 and self.maxHeap[temp] > self.maxHeap[(temp - 1) // 2]:
            self.maxHeap[temp], self.maxHeap[(temp - 1) // 2] = self.maxHeap[(temp - 1) // 2], self.maxHeap[temp]
            temp = (temp - 1) // 2
    def maxHeapPop(self):
        res = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap[-1]
        self.maxHeap.pop()
        length = len(self.maxHeap)
        temp = 0
        nextNode = 2 * temp + 1
        while nextNode < length:
            if nextNode + 1 < length and self.maxHeap[nextNode + 1] > self.maxHeap[nextNode]:
                nextNode += 1
            if self.maxHeap[nextNode] > self.maxHeap[temp]:
                self.maxHeap[nextNode], self.maxHeap[temp] = self.maxHeap[temp], self.maxHeap[nextNode]
                temp = nextNode
                nextNode = 2 * nextNode + 1
            else:
                break
        return res
    def minHeapInsert(self, number):
        self.minHeap.append(number)
        length = len(self.minHeap)
        temp = length - 1
        while (temp - 1) // 2 >= 0 and self.minHeap[temp] < self.minHeap[(temp - 1) // 2]:
            self.minHeap[temp], self.minHeap[(temp - 1) // 2] = self.minHeap[(temp - 1) // 2], self.minHeap[temp]
            temp = (temp - 1) // 2
    def minHeapPop(self):
        res = self.minHeap[0]
        self.minHeap[0] = self.minHeap[-1]
        self.minHeap.pop()
        length = len(self.minHeap)
        temp = 0
        nextNode = 2 * temp + 1
        while nextNode < length:
            if nextNode + 1 < length and self.minHeap[nextNode + 1] < self.minHeap[nextNode]:
                nextNode += 1
            if self.minHeap[nextNode] < self.minHeap[temp]:
                self.minHeap[nextNode], self.minHeap[temp] = self.minHeap[temp], self.minHeap[nextNode]
                temp = nextNode
                nextNode = 2 * nextNode + 1
            else:
                break
        return res
    def Insert(self, num):
        # 相加是偶数,先放入最小堆
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            if len(self.minHeap) > 0 and num > self.minHeap[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)
        else:
            if len(self.maxHeap) > 0 and num < self.maxHeap[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
    def GetMedian(self, n):
        if (len(self.minHeap) + len(self.maxHeap)) == 0:
            return None
        # 取平均值
        elif (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] + self.maxHeap[0]) / 2
        else:
            return self.maxHeap[0]

if __name__ == '__main__':
    s = Solution()
    l = [5,2,3,4,1,6,7,0,8]
    for i in l:
        s.Insert(i)
    print(s.GetMedian(0))