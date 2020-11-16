# 有向图送商品，从1送到5，从5返回到1，求T次配送最短距离。
from collections import defaultdict, deque

# bfs
if __name__ == '__main__':
    while True:
        try:
            # n个点、m条单向路径、T次配送
            n, m, T = map(int, input().split())
            go_dict = defaultdict(list)
            for i in range(m):
                start, end, length = map(int, input().split())
                go_dict[start].append((end, length))

            def bfs(res, visited, queue, final):
                while queue:
                    cur, cur_len = queue.popleft()
                    for next_node, len in go_dict[cur]:
                        next_len = cur_len + len
                        if next_node == final:
                            res = min(res, next_len)
                            continue
                        # 剪枝，如果遍历到当前节点（非终点）的长度next_len已经大于等于res了，则说明当前节点不可能是最优路径的中间节点
                        # 如果 next_len < res 且 当前节点没有被遍历或者当前有到达该节点更优的路径，则更新
                        if next_len < res and (next_node not in visited or visited[next_node] > next_len):
                            visited[next_node] = next_len
                            queue.append((next_node, next_len))
                return res
            res_1 = bfs(float('inf'), {1: 0}, deque([(1, 0)]), 5)
            res_2 = bfs(float('inf'), {5: 0}, deque([(5, 0)]), 1)
            print((res_1 + res_2) * T)

        except:
            break