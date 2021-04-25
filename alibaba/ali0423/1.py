from collections import defaultdict

l = list(map(int, input().split()))
# n * m矩阵, q次操作
n, m, q = l[0], [1], [2]
array = []
# 存储长度:行、左右指针
d = defaultdict(list)
# (行、左右指针):长度
dd = defaultdict(int)
for _ in range(n):
    temp = list(map(int, input().split()))
    array.append(temp)
res = []
# 统计每一行最长连续1的左右坐标
init = [[] for i in range(n)]
# 最长长度
max_val = 0
for i in range(n):
    left, right = 0, 0
    while left < m:
        if array[i][left] == 0:
            left += 1
        else:
            right = left + 1
            while right < m:
                if array[i][right] == 1:
                    right += 1
                else:
                    break
            init[i].append((left, right - 1))
            d[right - left].append((i, left, right - 1))
            dd[(i, left, right - 1)] = right - left
            max_val = max(max_val, right - left)
            left = right

for _ in range(q):
    ll = list(map(int, input().split()))
    i, j = ll[0], ll[1]
    if array[i - 1][j - 1] == 0:
        array[i - 1][j - 1] = 1

    elif array[i - 1][j - 1] == 1:
        array[i - 1][j - 1] = 0
        for k, (start, end) in enumerate(init[i - 1]):
            if j - 1 == start:
                if start == end:
                    init[i - 1].remove((start, end))
                else:
                    init[i - 1][k] = (start + 1, end)
            elif j - 1 == end:
                if start == end:
                    init[i - 1].remove((start, end))
                else:
                    init[i - 1][k] = (start, end - 1)
            elif start < j - 1 < end:
                temp = (j, end)
                init[i - 1][k] = (start, j - 2)
                init[i - 1].insert(k + 1, (j, end))

