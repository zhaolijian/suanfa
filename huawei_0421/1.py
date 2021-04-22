l = list(map(int, input().split()))
# N为电话预约数量, M为桌位,如果预约人数超过30,则本次预约作废
N, M = l[0], l[1]
array = []
for _ in range(N):
    temp = list(map(int, input().split()))
    array.append(temp)
res = [0] * 24
for start, end, number in array:
    # 是否会超出桌位
    flag = True
    for i in range(start, end):
        res[i] += number
        if res[i] > M:
            flag = False
    if not flag:
        for i in range(start, end):
            res[i] -= number
print(" ".join(map(str, res)))