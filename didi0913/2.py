# 题目描述：
# 小滴正在筹划他的毕业旅行。他打算去找他的外国网友们，首先第一站是法国巴黎，但是去巴黎的路线有很多，交通工具也有很多可供选择。
# 现在有一个结点数为n，边的条数为m的无向图表示小滴到巴黎的所有路线。
# 其中小滴的家为结点s，巴黎为结点e，小滴出发时间为start，请问小滴最早什么时候能到达巴黎？
# 输入描述
# 单组输入，数字间有空格隔开。
# 第一行两个整数：结点数n，边数m（n<=1000,m<=10000）。
# 第二行到第m+1行每行各有三个整数：结点u，结点v，需要的时间time（1<=u,v<=n，time<50，time以小时为单位）。
# 最后一行为家的位置：s，巴黎的位置：e，出发时间start（1<=s,e<=n，出发时间格式为month.day/hour，小时为24小时制，出发年份默认为2020年，且一定会在2020年到达，数据保证有解。）
# 输出描述
# 最早能到达巴黎的时间e time（格式与出发时间格式相同）。
#
# 样例输入
# 4 4
# 1 2 5
# 1 3 6
# 2 4 8
# 3 4 6
# 1 4 7.9/8
# 样例输出
# 7.9/20
#
# 提示
# 输入样例2
# 4 4
# 1 2 25
# 1 3 18
# 2 4 28
# 3 4 22
# 1 4 7.9/8
#
# 输出样例2
# 7.11/0
from collections import defaultdict
if __name__ == '__main__':
    while True:
        try:
            # 节点、边数
            n, m = map(int, input())
            times = {}
            sons = defaultdict(list)
            for i in range(m):
                first, second, time = map(int, input().split())
                times[(first, second)] = time
                times[(second, first)] = time
                sons[first].append(second)
                sons[second].append(first)
            end_line = list(input().split())
            start, end = end_line[0], end_line[1]
            start_time = end_line[2]
            res = []
            visisted = set()
            visisted.add(start)

            def func(start, end, cur_time):
                if start == end:
                    res.append(cur_time)
                    return
                for son in sons[start]:
                    if son not in visisted:
                        visisted.add(son)
                        func(son, end, cur_time + times[(start, son)])
                        visisted.remove(son)

            func(start, end, 0)
            min_time = min(res)
            print(min_time)
        except:
            break