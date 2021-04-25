T = int(input())
for _ in range(T):
    # 旗子和球的数量
    n = int(input())
    # 每个旗子面前的球的颜色
    ll = list(map(int, input().split()))
    l, r = 0, 0
    for i in range(n):
        if ll[i] != i + 1:
            l = i
            break
    for i in range(n - 1, -1, -1):
        if ll[i] != i + 1:
            r = i
            break
    # 需要调整的区间为[l,r]
    # 看下这个区间是否是两个有序区间拼接起来的
    # 后者比前者小的次数
    number = 0
    min_index = l
    for i in range(l + 1, r + 1):
        if ll[i] < ll[i - 1]:
            number += 1
            min_index = i
    if number == 0:
        print(0)
    elif number > 1:
        print(-1)
    else:
        res = [l + 1, r + 1, min_index - l]
        print(' '.join(map(str, res)))