# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
# 你需要计算完成所有任务所需要的 最短时间 。


# 桶排序
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        ct = Counter(tasks)
        # 出现次数最多的一个组成一个list，选择list中的第一个，选择list中第一个元素的第二个位置
        # Counter('abcdeabcdabcaba').most_common(3)
        # [('a', 5), ('b', 4), ('c', 3)]
        # 出现最多的次数
        nbucket = ct.most_common(1)[0][1]
        # 出现最多次数的元素个数
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))


from collections import Counter
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        counter = Counter(tasks)
        max_vlaue = 0
        # 最多数量
        for key in counter.keys():
            if counter[key] > max_vlaue:
                max_vlaue = counter[key]
        # 最多数量对应的种类数量
        number = 0
        for key in counter.keys():
            if max_vlaue == counter[key]:
                number += 1
        res = (max_vlaue - 1) * (n + 1) + number
        return max(res, len(tasks))


# 方法2 使用最大堆解决，效率比较低
# from heapq import heapify, heappush, heappop
# from collections import Counter
# class Solution:
#     def leastInterval(self, tasks, n: int) -> int:
#         res = 0
#         counter = Counter(tasks)
#         array = []
#         for key in counter:
#             array.append((-counter[key], key))
#         # 临时存放中最小堆中取出来的元素
#         temp = []
#         # 构建负数的最小堆即最大堆
#         heapify(array)
#         while array or temp:
#             # 时间
#             number = 0
#             while array:
#                 if number <= n:
#                     val, ele = heappop(array)
#                     if val < - 1:
#                         temp.append((val + 1, ele))
#                     number += 1
#                     res += 1
#                 else:
#                     break
#             if temp and number < n + 1:
#                 res += n + 1 - number
#             while temp:
#                 heappush(array, temp.pop())
#         return res


if __name__ == '__main__':
    s = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(s.leastInterval(tasks, n))
