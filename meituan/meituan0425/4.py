l = list(map(int, input().split()))
# 线的数量，敌人的数量，小美的子弹数
n, m, k = l[0], l[1], l[2]
# 可以开枪的时间
times = list(map(int, input().split()))
for _ in range(m):
    temp = list(map(int, input().split()))
    # 这个敌人到达的时间和到达的行数
    t, r = temp[0], temp[1]
print(-1)