# 王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
# 主件	附件
# 电脑	打印机，扫描仪
# 书柜	图书
# 书桌	台灯，文具
# 工作椅	无
# 如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：用整数 1 ~ 5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
#     设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
# v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
#     请你帮助王强设计一个满足要求的购物单。


from collections import defaultdict
N, m = map(int, input().split())
# 每个物品的价格、价值(价格*权重)
w, v = [], []
primary_ = {}
other = defaultdict(list)
for i in range(m):
    money, weight, primary = map(int, input().split())
    if primary == 0:
        primary_[i] = (money, weight)
    else:
        other[primary - 1].append((money, weight))
for key in primary_.keys():
    temp_w = []
    temp_v = []
    primary_w, primary_v = primary_[key][0], primary_[key][0] * primary_[key][1]
    temp_w.append(primary_w)
    temp_v.append(primary_v)
    length = len(other[key])
    if length > 0:
        other1_w, other1_v = primary_w + other[key][0][0], primary_v + other[key][0][0] * other[key][0][1]
        temp_w.append(other1_w)
        temp_v.append(other1_v)
        if length > 1:
            temp_w.append(other1_w + other[key][1][0])
            temp_v.append(other1_v + other[key][1][0] * other[key][1][1])
    w.append(temp_w)
    v.append(temp_v)
length_primary = len(primary_.keys())
# 纵坐标主件、横坐标价格
dp = [[0 for i in range(N + 1)] for j in range(length_primary + 1)]
for i in range(1, length_primary + 1):
    for j in range(0, N + 1, 10):
        temp = dp[i - 1][j]
        for p in range(len(w[i - 1])):
            if j >= w[i - 1][p]:
                temp = max(temp, dp[i - 1][j - w[i - 1][p]] + v[i - 1][p])
        dp[i][j] = temp
print(dp[-1][-1])

