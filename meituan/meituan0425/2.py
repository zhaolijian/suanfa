# 题目描述：
# 小美有一个由小写字母组成的字符串。小美认为字母表很有意思。所以他规定，在小写字母中，每个字母的后继就是字母表中这个字母的后一个，比如a的后继是b，b的后继是c。而字母表中的最后一个字母是z，为了防止z没有后继，小美又规定z的后继是a。这样字母的后继就形成了一个闭环。
#
# 现在小美想要让字符串发生变化。所以他每次会给出一个区间和一个数k，并且让区间中所有的字母变成他们的第k个后继。第k个后继即让后继操作进行k次，比如a的2级后继是c，a的26级后继是a。
#
# 现在小美记下来了操作序列和操作完之后得到的字符串。请你还原原来的字符串。
#
#
#
# 输入描述
# 第一行一个长度为n(1≤n≤105)的字符串，代表操作完成之后得到的字符串。
#
# 第二行一个数q(1≤q≤105)，代表操作次数。
#
# 接下来q行，每行三个数l,r,k(1≤l≤r≤n,1≤k≤109)。代表区间的左右端点和第k级后继。
#
# 输出描述
# 输出一个字符串，代表操作之前小美的字符串。
# s = input()
# length = len(s)
# # 操作次数
# q = int(input())
# array = []
# for _ in range(q):
#     ll = list(map(int, input().split()))
#     array.append(ll)
# res = ""
# for l, r, k in array[::-1]:
#     for i in range(l - 1):
#         res += s[i]
#     for i in range(l - 1, r):
#         # s[i]左移k个位置
#         temp = ord(s[i]) - k % 26
#         if temp < ord('a'):
#             temp += 26
#         res += chr(temp)
#     for i in range(r, length):
#         res += s[i]
#     s = res
#     res = ""
# print(s)


s = input()
length = len(s)
# 操作次数
q = int(input())
array = []
for _ in range(q):
    ll = list(map(int, input().split()))
    array.append(ll)
res = ""
for l, r, k in array[::-1]:
    res += s[:l-1]
    for i in range(l - 1, r):
        # s[i]左移k个位置
        temp = ord(s[i]) - k % 26
        if temp < 97:
            temp += 26
        res += chr(temp)
    res += s[r:]
    s = res
    res = ""
print(s)