# 题目描述：
# D星群岛由n个小岛组成。为了加强小岛居民之间的交流，头目决定启动一个造桥工程，将全部n个岛连接到一起。
# 由于受到金融危机的影响，头目要求造桥的总成本要最少，并且还规定每一座桥的成本都不能超过k万D星币。
# 需要注意的是，由于受到地理环境和气候影响，有些小岛之间没有办法直接造桥。
# 现在给你m条小岛之间的造桥成本数据以及k的值，请问这个宏伟的造桥工程是否能够顺利完成？
# 注意：可能边不够，也可能费用超支。
#
# 输入描述
# 多组输入，第1行输入一个正整数T表示输入数据的组数。
# 对于每一组输入数据：输入m+1行。
# 第1行包含三个正整数，分别表示n、m和k，n≤100，m≤1000，k≤10000，三个数字之间用空格隔开。
# 接下来m行表示m条小岛之间的造桥成本数据，每一行包含三个正整数，分别表示两个小岛的编号（从1开始）和这两个小岛之间的造桥成本（单位：万）。
# 输出描述
# 针对每一组输入数据，如果能够完成造桥工程输出“Yes”，否则输出“No”。
# 样例输入
# 2
# 3 3 400
# 1 2 200
# 1 3 300
# 2 3 500
# 3 3 400
# 1 2 500
# 1 3 600
# 2 3 700
# 样例输出
# Yes
# No
# if __name__ == '__main__':
#     T = int(input())
#     for _ in range(T):
#         # 小岛数、桥数据、每个桥最高花费
#         n, m, k = map(int, input().split())
#         # 岛数
#         s = set()
#         parent = {}
#
#         def find(x):
#             if parent[x] == x:
#                 return x
#             parent[x] = find(parent[x])
#             return parent[x]
#
#         for i in range(m):
#             start, end, cost = map(int, input().split())
#             s.add(start)
#             s.add(end)
#             if cost <= k:
#                 parent[end] = start
#
#         if len(s) < n:
#             print('No')
#             continue
#         # 使用并查集将所有低于k的桥连接的岛放到一起
#         res = set()
#         for i in s:
#             res.add(find(i))
#         if len(res) > 1:
#             print('No')
#         else:
#             print('Yes')

from collections import defaultdict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        # 小岛数、桥数据、每个桥最高花费
        n, m, k = map(int, input().split())
        parent = defaultdict(list)

        for i in range(m):
            start, end, cost = map(int, input().split())
            if cost <= k:
                parent[start].append(end)
                parent[end].append(start)

        array = [1]
        while array:
            for i in range(len(array)):
                temp = array.pop(0)
                if temp not in parent[1]:
                    for son in parent[temp]:
                        array.append(son)
                    parent[1].append(temp)
        if len(parent[1]) >= n:
            print('Yes')
        else:
            print('No')