# 给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，
# 其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。
# 指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。
# 如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。


# BFS
# 从源点出发，每次选择最短的路径终点，然后往后一个未访问过的节点扩展，如果扩展到目标节点则可以直接返回。
from collections import deque, defaultdict

class Solution:
    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:
        if not edges or not edges[0]:
            return 0

        # 构造节点邻接表
        st_maps = defaultdict(list)
        for i, (s, e) in enumerate(edges):
            st_maps[s].append((e, succProb[i]))
            st_maps[e].append((s, succProb[i]))

        ans = 0
        # 到某个节点的概率值
        queue = deque([(start, 1)])
        #
        visited = {start: 1}
        while queue:
            # 当前节点
            cur_node, cur_prob = queue.popleft()
            for next_node, p in st_maps[cur_node]:
                # 下一个待遍历的节点
                next_prob = cur_prob * p
                if next_node == end:
                    ans = max(ans, next_prob)
                    continue

                # 剪枝和去重：如果下一个待遍历节点的概率大于ans(说明该节点有希望成为最佳路径中的一个节点)
                # && (该节点未遍历过 或 遍历过该节点但是上次的概率比现在小)
                # 当有环的时候,乘积会越来越小,该语句next_prob > res会将之筛出去
                if next_prob > ans and (next_node not in visited or visited[next_node] < next_prob):
                    visited[next_node] = next_prob
                    queue.append((next_node, next_prob))
        return ans


# 方法2 dijkstra


if __name__ == '__main__':
    s = Solution()
    n = 3
    edges = [[0,1]]
    succProb = [0.5]
    start = 0
    end = 2
    print(s.maxProbability(n, edges, succProb, start, end))