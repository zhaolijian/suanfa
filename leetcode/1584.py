# 给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。
# 连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的 曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。
# 请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。

class Solution:
    def minCostConnectPoints(self, points) -> int:
        def find(index):
            if parents[index] == index:
                return index
            parents[index] = find(parents[index])
            return parents[index]

        d = {}
        length = len(points)
        if length < 2:
            return 0
        parents = {}
        for i in range(length):
            parents[i] = i
        for i in range(length):
            for j in range(i + 1, length):
                temp = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                d[(i, j)] = temp
        l = sorted(d.items(), key=lambda item: item[1])
        res = 0
        number = 0
        for ele, val in l:
            start, end = ele[0], ele[1]
            # 如果祖先节点一样的话,那么连接后就会形成环路
            if find(start) != find(end):
                res += val
                number += 1
                if number == length - 1:
                    return res
                parents[find(end)] = find(start)

if __name__ == '__main__':
    s = Solution()
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    print(s.minCostConnectPoints(points))