#小美有一个新的电子琴。这个电子琴在弹奏时分为26个大调，用字母A-Z表示。每个大调内有c个音。所有音符完成排名之后，每次询问给出一个排名，你需要帮助小美知道这个排名对应的是哪个音符。

#
#
# 输入描述
# 第一行两个数n,c(1≤n,c≤105)，代表有n个询问，每个大调内有c个音。
#
# 接下来每一行代表一次询问，由一个数字代表一个音符的排名。
#
# 输出描述
# 对每个询问输出一行，先是一个大写字母代表大调，接着一个数字代表这个音在这个大调内的序号。
# l = list(map(int, input().split()))
# # n个询问、每个大调c个音
# n, c = l[0], l[1]
# for _ in range(n):
#     number = int(input())
#     zhengshu = number // c
#     # 如果余数为0,则输出c
#     yushu = number % c
#     if yushu == 0:
#         res1 = chr(ord("A") + zhengshu - 1)
#         res2 = str(c)
#     else:
#         res1 = chr(ord("A") + zhengshu)
#         res2 = str(yushu)
#     print(res1 + res2)
#5 5
# 71
# 28
# 120
# 30
# 1
# 样例输出
import sys

sys.stdout(1)