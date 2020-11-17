# 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
# 另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
# 返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，
# 其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）

from collections import defaultdict


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        res = []
        d = defaultdict(list)
        for i in range(R):
            for j in range(C):
                temp = abs(i - r0) + abs(j - c0)
                d[temp].append([i, j])
        for i in range(200):
            if i in d:
                res += d[i]
            # 加上该句，更加优化，不加也没事，如果存在更大的曼哈顿距离，肯定会连续，不可能有一个曼哈顿距离是x，没有x+1，有x+2
            else:
                break
        return res


# 正统的桶排序
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        res = []
        init = [[] for i in range(200)]
        for i in range(R):
            for j in range(C):
                temp = abs(i - r0) + abs(j - c0)
                init[temp].append([i, j])
        for ele in init:
            if ele:
                res += ele
            else:
                break
        return res
