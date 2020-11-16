# 李华顺利地到达了巴黎，他的好友Peter带他开启了他的巴黎之旅。
#
# 途中，李华遇到了许多心动的纪念品想要带回家，但是他又不想自己太累，而且他买纪念品也有相应的预算k，现给出他心动的纪念品清单：共有n件，其中每件都各有其价格price，重量weight，心动值v(其中心动值为1~5之间的数值)，需要注意的是：在心动值不同的情况下，李华会优先选择心动值大的纪念品；若心动值相同，李华会优先选择比较便宜的纪念品，具体见样例。同时给出李华在保证不累的情况下，最多能拿的物品重量m。在不超过预算并且保证不累的情况下，李华最多可以带几件纪念品回家？
# 输入描述
# 单组输入。
#
# 第1行三个正整数，分别为：纪念品件数n，最多能拿的物品重量m，预算k。（n<1e5,m<100,k<10000,k的单位为元，m的重量为kg）
#
# 第2行到第n+1行，分别为每件物品的价格price，重量weight，心动值v。（price<10000,weight<100,v为1~5之间的整数，price的单位为元，weight的重量为kg）
#
# 输出描述
# 在不超过预算并且保证不累的情况下，李华最多可以带回家的纪念品件数。
from collections import defaultdict

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    d = defaultdict(list)
    for _ in range(n):
        price, weight, v = map(int, input().split())
        d[v].append((price, weight))
    for key in d.keys():
        d[key].sort()
    if n <= 0 or m <= 0 or k <= 0:
        print(0)
    res = 0
    for i in range(5, 0, -1):
        if i in d:
            for p, w in d[i]:
                if p <= k and w <= m:
                    res += 1
                    k -= p
                    m -= w
    print(res)