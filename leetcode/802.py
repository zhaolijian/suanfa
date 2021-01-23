# 在有向图中, 我们从某个节点和每个转向处开始, 沿着图的有向边走。 如果我们到达的节点是终点 (即它没有连出的有向边), 我们停止。
# 现在, 如果我们最后能走到终点，那么我们的起始节点是最终安全的。 更具体地说, 存在一个自然数 K,  无论选择从哪里开始行走, 我们走了不到 K 步后必能停止在一个终点。
# 哪些节点最终是安全的？ 结果返回一个有序的数组。
# 该有向图有 N 个节点，标签为 0, 1, ..., N-1, 其中 N 是 graph 的节点数.  图以以下的形式给出: graph[i] 是节点 j 的一个列表，满足 (i, j) 是图的一条有向边。


class Solution:
    def eventualSafeNodes(self, graph):
        # graph中至少有一个为空，否则肯定会循环
        flag = False
        for ele in graph:
            if not ele:
                flag = True
        if not flag:
            return []
        res = []

        # 当前节点、最开始节点
        def dfs(node, init_node):
            if not graph[node]:
                return True
            for ele in graph[node]:
                if ele == init_node or ele == node:
                    return False
                if not dfs(ele, init_node):
                    return False
            return True

        length = len(graph)
        for i in range(length):
            if dfs(i, i):
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    graph = [[1,2,3,4],[2,4],[0,3,4],[2],[]]
    print(s.eventualSafeNodes(graph))