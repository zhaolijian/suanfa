# 数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，
# 即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
number = int(input())
d = {}
for i in range(number):
    x, y = map(int, input().split())
    if x in d:
        d[x] += y
    else:
        d[x] = y
array = sorted(d.items(), key=lambda x: x[0])
for i in range(len(array)):
    print(array[i][0], end=' ')
    print(array[i][1])