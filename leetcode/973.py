# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
# （这里，平面上两点之间的距离是欧几里德距离。）
# 你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

# 该题虽然是让求欧式距离，但是直接通过平方和的形式比较即可，不用开方

# 方法1 最小堆，即使用负数的最大堆
import heapq
class Solution:
    def kClosest(self, points, K: int):
        list = []
        res = []
        heapq.heapify(list)
        for i, point in enumerate(points):
            temp = pow(point[0], 2) + pow(point[1], 2)
            if i < K:
                heapq.heappush(list, (-temp, point))
            else:
                heapq.heappushpop(list, (-temp, point))
        for val, point in list:
            res.append(point)
        return res


# 方法2 排序
# class Solution:
#     def kClosest(self, points, K: int):
#         points.sort(key=lambda x: pow(x[0], 2) + pow(x[1], 2))
#         return points[:K]


# 方法2
# from collections import defaultdict
# class Solution:
#     def kClosest(self, points, K: int):
#         res = []
#         number = 0
#         d = defaultdict(list)
#         for first, second in points:
#             temp = pow(first, 2) + pow(second, 2)
#             d[temp].append([first, second])
#         for key in sorted(d.keys()):
#             for ele in d[key]:
#                 res.append(ele)
#                 number += 1
#                 if number >= K:
#                     return res

