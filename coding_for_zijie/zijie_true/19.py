# 题目描述
# 小明目前在做一份毕业旅行的规划。打算从北京出发，分别去若干个城市，然后再回到北京，每个城市之间均乘坐高铁，且每个城市只去一次。由于经费有限，希望能够通过合理的路线安排尽可能的省一些路上的花销。给定一组城市和每对城市之间的火车票的价钱，找到每个城市只访问一次并返回起点的最小车费花销。
# 输入描述:
# 城市个数n（1<n≤20，包括北京）
#
# 城市间的车票价钱 n行n列的矩阵 m[n][n]
# 输出描述:
# 最小车费花销 s

# 方法1 dfs
n = int(input())
array = []
for _ in range(n):
    temp = list(map(int, input().split()))
    array.append(temp)
def func(index, cost):
    global res
    if len(visisted) == n:
        res = min(res, cost + array[index][0])
        return
    for i in range(n):
        if array[index][i] and i not in visisted:
            visisted.add(i)
            func(i, cost + array[index][i])
            visisted.remove(i)

res = float('inf')
visisted = set()
visisted.add(0)
func(0, 0)
print(res)


# 方法2 dp
