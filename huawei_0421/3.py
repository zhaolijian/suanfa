from collections import defaultdict
# 供暖站最大跳数
K = int(input())
# 不同跳数的建设成本
cost = []
for _ in range(K):
    cost.append(int(input()))
l = list(map(int, input().split()))
# 供暖节点数、边数
N, E = l[0], l[1]
d = defaultdict(list)
for _ in range(E):
    temp = list(map(int, input().split()))
    d[temp[0]].append(temp[1])
res = float('inf')
# 每个节点距离其他节点的跳数
print(cost[0])