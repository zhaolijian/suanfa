# 题目描述
# 为了不断优化推荐效果，今日头条每天要存储和处理海量数据。假设有这样一种场景：我们对用户按照它们的注册时间先后来标号，对于一类文章，
# 每个用户都有不同的喜好值，我们会想知道某一段时间内注册的用户（标号相连的一批用户）中，有多少用户对这类文章喜好值为k。
# 因为一些特殊的原因，不会出现一个查询的用户区间完全覆盖另一个查询的用户区间(不存在L1<=L2<=R2<=R1)。
# 输入描述:
# 输入： 第1行为n代表用户的个数 第2行为n个整数，第i个代表用户标号为i的用户对某类文章的喜好度
# 第3行为一个正整数q代表查询的组数  第4行到第（3+q）行，每行包含3个整数l,r,k代表一组查询，
# 即标号为l<=i<=r的用户中对这类文章喜好值为k的用户的个数。 数据范围n <= 300000,q<=300000 k是整型
# 输出描述:
# 输出：一共q行，每行一个整数代表喜好值为k的用户的个数
from collections import defaultdict
# 用户数
n = int(input())
# 用户对文章的喜好度
like = list(map(int, input().split()))
d = defaultdict(list)
for i in range(n):
    d[like[i]].append(i)
for key in d.keys():
    d[key].sort()
# 查询的组数
q = int(input())
res = []
for _ in range(q):
    l, r, k = map(int, input().split())
    temp = 0
    for ele in d[k]:
        if ele + 1 < l:
            continue
        elif ele + 1 > r:
            break
        else:
            temp += 1
    res.append(temp)
for ele in res:
    print(ele)