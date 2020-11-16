# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

# 方法1 迭代法 看清本质：岛屿的周长即为岛屿和水的相交边的数量 时间复杂度O(mn)， 空间复杂度O(1)
# class Solution:
#     def islandPerimeter(self, grid) -> int:
#         heigth = len(grid)
#         if heigth == 0:
#             return 0
#         width = len(grid[0])
#         res = 0
#         move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         for i in range(heigth):
#             for j in range(width):
#                 if grid[i][j] == 1:
#                     for mx, my in move:
#                         temp_x, temp_y = i + mx, j + my
#                         if temp_x < 0 or temp_x >= heigth or temp_y < 0 or temp_y >= width or grid[temp_x][temp_y] == 0:
#                             res += 1
#         return res


# 方法2 dfs
# class Solution:
#     def islandPerimeter(self, grid) -> int:
#         heigth = len(grid)
#         if heigth == 0:
#             return 0
#         width = len(grid[0])
#         res = 0
#         move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         visited = set()
#
#         init_x, init_y, flag = 0, 0, True
#         for i in range(heigth):
#             if flag:
#                 for j in range(width):
#                     if grid[i][j] == 1:
#                         init_x, init_y = i, j
#                         visited.add((init_x, init_y))
#                         flag = False
#                         break
#
#         def dfs(i, j):
#             nonlocal res
#             for mx, my in move:
#                 temp_x, temp_y = i + mx, j + my
#                 if 0 <= temp_x < heigth and 0 <= temp_y < width:
#                     if grid[temp_x][temp_y] == 1 and (temp_x, temp_y) not in visited:
#                         visited.add((temp_x, temp_y))
#                         dfs(temp_x, temp_y)
#                     elif grid[temp_x][temp_y] == 0:
#                         res += 1
#                 else:
#                     res += 1
#
#         dfs(init_x, init_y)
#         return res



# 方法3 bfs
class Solution:
    def islandPerimeter(self, grid) -> int:
        heigth = len(grid)
        if heigth == 0:
            return 0
        width = len(grid[0])
        res = 0
        move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        flag = True
        array = []
        for i in range(heigth):
            if flag:
                for j in range(width):
                    if grid[i][j] == 1:
                        array.append((i, j))
                        visited.add((i, j))
                        flag = False
                        break
        while array:
            x, y = array.pop()
            for mx, my in move:
                temp_x, temp_y = mx + x, my + y
                if temp_x < 0 or temp_x >= heigth or temp_y < 0 or temp_y >= width or grid[temp_x][temp_y] == 0:
                    res += 1
                elif (temp_x, temp_y) not in visited:
                    array.append((temp_x, temp_y))
                    visited.add((temp_x, temp_y))
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(s.islandPerimeter(grid))