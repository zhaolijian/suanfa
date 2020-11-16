# 题目描述
# 作为一个手串艺人，有金主向你订购了一条包含n个杂色串珠的手串——每个串珠要么无色，要么涂了若干种颜色。
# 为了使手串的色彩看起来不那么单调，金主要求，手串上的任意一种颜色（不包含无色），
# 在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。手串上的颜色一共有c种。
# 现在按顺时针序告诉你n个串珠的手串上，每个串珠用所包含的颜色分别有哪些。请你判断该手串上有多少种颜色不符合要求。
# 即询问有多少种颜色在任意连续m个串珠中出现了至少两次。
# 输入描述:
# 第一行输入n，m，c三个数，用空格隔开。(1 <= n <= 10000, 1 <= m <= 1000, 1 <= c <= 50)
# 接下来n行每行的第一个数num_i(0 <= num_i <= c)表示第i颗珠子有多少种颜色。
# 接下来依次读入num_i个数字，每个数字x表示第i颗柱子上包含第x种颜色(1 <= x <= c)
# 输出描述:
# 一个非负整数，表示该手链上有多少种颜色不符需求。
from collections import defaultdict
# n个珠子、任意连续的m个串珠、手串颜色c种
n, m, c = map(int, input().split())
# 颜色对应的珠子列表字典
d = defaultdict(list)
for i in range(n):
    temp = list(map(int, input().split()))
    colors = temp[0]
    for j in range(1, colors + 1):
        d[temp[j]].append(i)
res = 0
for key, l in d.items():
    l.sort()
    length = len(l)
    if length < 2:
        continue
    flag = False
    for i in range(1, length):
        if l[i] - l[i - 1] < m:
            flag = True
            break
    if flag:
        res += 1
    else:
        head, tail = l[0] + n, l[-1]
        if head - tail < m:
            res += 1
print(res)