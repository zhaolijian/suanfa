# 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
# 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。
# 请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。

# 如果线数<n-1,则返回-1
# 否则线数肯定够，返回连通分量数-1
class Solution:
    def makeConnected(self, n: int, connections) -> int:
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            nonlocal res
            root_1, root_2 = find(node1), find(node2)
            # 根节点不同，则说明不是一个连通分量
            if root_1 != root_2:
                parent[find(node2)] = find(node1)
                res -= 1

        if len(connections) < n - 1:
            return -1
        parent = [i for i in range(n)]
        # 初始化连通分量数为节点数n
        res = n
        for first, second in connections:
            union(first, second)
        return res - 1
