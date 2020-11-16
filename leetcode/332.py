# 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，
# 对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
# 如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。
# 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
# 所有的机场都用三个大写字母表示（机场代码）。
# 假定所有机票至少存在一种合理的行程。

# 方法：Hierholzer 算法
# Hierholzer 算法用于在连通图中寻找欧拉路径，其流程如下：
# 1.从起点出发，进行深度优先搜索。
# 2.每次沿着某条边从某个顶点移动到另外一个顶点的时候，都需要删除这条边。
# 3.如果没有可移动的路径，则将所在节点加入到栈中，并返回。

import collections
class Solution:
    def findItinerary(self, tickets):
        d = collections.defaultdict(list)   #邻接表
        for f, t in tickets:
            d[f] += [t]         #路径存进邻接表
        for f in d:
            d[f].sort()         #邻接表排序
        ans = []

        def dfs(f):             #深搜函数
            while d[f]:
                dfs(d[f].pop(0))#路径检索
            # 往深里找找不到说明该机场为最终降落机场，
            ans.insert(0, f)    #放在最前
        dfs('JFK')
        return ans


# 或
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        d = defaultdict(list)
        for start, end in tickets:
            d[start].append(end)
        for ele in d:
            d[ele].sort()
        res = []
        def dfs(node):
            nonlocal res
            while d[node]:
                dfs(d[node].pop(0))
            res = [node] + res
        dfs('JFK')
        return res


if __name__ == '__main__':
    s = Solution()
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print(s.findItinerary(tickets))