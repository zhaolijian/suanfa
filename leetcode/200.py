# 岛屿数量
class Solution:
    # 求矩阵中1通过横向/纵向连接到一块区域的数量，斜线不算
    # 方法是使用深度优先遍历/广度优先遍历
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        h, w = len(grid), len(grid[0])
        res = 0

        def func(i, j):
            if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            func(i - 1, j)
            func(i + 1, j)
            func(i, j - 1)
            func(i, j + 1)

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    res += 1
                    func(i, j)
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(grid))