# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
# （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
# 返回区域的数目。


class Solution:
    def regionsBySlashes(self, grid) -> int:
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            nonlocal res
            root_1, root_2 = find(node1), find(node2)
            if root_1 != root_2:
                parent[find(node2)] = find(node1)
                res -= 1

        N = len(grid)
        # 将每个方格通过两个对角线划分为四块,上右下左分别为0,1,2,3.使用并查集向右向下合并
        size = 4 * N * N
        parent = [i for i in range(size)]
        # 返回的是连通集的个数
        res = size
        for i in range(N):
            row = list(grid[i])
            for j in range(N):
                # 二维网格转化为一维网格
                index = 4 * (i * N + j)
                c = row[j]
                # 单元格内合并
                if c == "/":
                    union(index, index + 3)
                    union(index + 1, index + 2)
                elif c == "\\":
                    union(index, index + 1)
                    union(index + 2, index + 3)
                else:
                    union(index, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)
                # 单元格间合并
                # 向右合并：1（当前）、3（右一列）
                if j < N - 1:
                    union(index + 1, index + 7)
                # 向下合并
                if i < N - 1:
                    union(index + 2, index + 4 * N)
        return res