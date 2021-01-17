# 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
# 给你一棵包含 n 个节点的数，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
# 可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
# 请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
# 树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。


# 拓扑排序(因为是无向图，所以最中间的节点便是高度最小树的根节点)，思路：从边缘开始，先找到所有出度为1的节点，然后把所有出度为1的节点进队列，然后不断地bfs，
# 最后找到的就是两边同时向中间靠近的节点，那么这个中间节点就相当于把整个距离二分了，那么它当然就是到两边距离最小的点啦，也就是到其他叶子节点最近的节点了。
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges):
        # 临接表(无向图的临接表能够同时表示入度和临接表)
        adjacent = defaultdict(list)
        for first, second in edges:
            adjacent[first].append(second)
            adjacent[second].append(first)
        array = []
        for key in adjacent.keys():
            if len(adjacent[key]) == 1:
                array.append(key)
        # 初始化edges为空的情况
        res = [0]
        while array:
            # 最后一次array即所求
            res = array.copy()
            for i in range(len(array)):
                temp = array.pop(0)
                for ele in adjacent[temp]:
                    adjacent[ele].remove(temp)
                    if len(adjacent[ele]) == 1:
                        array.append(ele)
        return res



# 纯bfs，超时
# from collections import defaultdict
# class Solution:
#     def findMinHeightTrees(self, n: int, edges):
#         if not edges:
#             return [0]
#
#         # 临接表
#         adjacent = defaultdict(list)
#         for first, second in edges:
#             adjacent[first].append(second)
#             adjacent[second].append(first)
#         res = n
#         # 返回的根节点数组
#         result = []
#         # 遍历,以每一节点为根节点
#         for i in range(n):
#             visisted = [0] * n
#             array = [i]
#             heigth = 0
#             while array:
#                 heigth += 1
#                 for j in range(len(array)):
#                     temp = array.pop(0)
#                     visisted[temp] = 1
#                     for ele in adjacent[temp]:
#                         if visisted[ele] == 0:
#                             array.append(ele)
#             if heigth < res:
#                 res = heigth
#                 result = [i]
#             elif heigth == res:
#                 result.append(i)
#         return result


# dfs超时
# from collections import defaultdict
# class Solution:
#     def findMinHeightTrees(self, n: int, edges):
#         if not edges:
#             return [0]
#
#         def dfs(root, heigth):
#             visisted[root] = 1
#             result = float('-inf')
#             for ele in adjacent[root]:
#                 if visisted[ele] == 0:
#                     cur_heigth = dfs(ele, heigth + 1)
#                     if cur_heigth > result:
#                         result = cur_heigth
#             return heigth + 1 if result == float('-inf') else result
#
#         # 临接表
#         adjacent = defaultdict(list)
#         for first, second in edges:
#             adjacent[first].append(second)
#             adjacent[second].append(first)
#         res = n
#         array = []
#         # 遍历,以每一节点为根节点
#         for i in range(n):
#             visisted = [0] * n
#             heigth = dfs(i, 0)
#             if heigth < res:
#                 res = heigth
#                 array = [i]
#             elif heigth == res:
#                 array.append(i)
#         return array


if __name__ == '__main__':
    s = Solution()
    n = 6
    edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
    print(s.findMinHeightTrees(n, edges))