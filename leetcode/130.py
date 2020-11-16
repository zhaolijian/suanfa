# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 方法1 深度优先遍历
# class Solution:
#     def solve(self, board) -> None:
#         def dfs(i, j):
#             if not 0 <= i < h or not 0 <= j < w or board[i][j] != 'O':
#                 return
#             board[i][j] = 'A'
#             dfs(i + 1, j)
#             dfs(i, j + 1)
#             dfs(i - 1, j)
#             dfs(i, j - 1)
#
#         if not board or not board[0]:
#             return
#         h, w = len(board), len(board[0])
#         for i in range(h):
#             dfs(i, 0)
#             dfs(i, w - 1)
#         for j in range(1, w - 1):
#             dfs(0, j)
#             dfs(h - 1, j)
#
#         for i in range(h):
#             for j in range(w):
#                 if board[i][j] == 'O':
#                     board[i][j] = 'X'
#                 elif board[i][j] == 'A':
#                     board[i][j] = 'O'



# 方法2 广度优先遍历
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        h, w = len(board), len(board[0])
        array = deque()
        for i in range(h):
            if board[i][0] == 'O':
                array.append((i, 0))
            if board[i][w - 1] == 'O':
                array.append((i, w - 1))
        for j in range(1, w - 1):
            if board[0][j] == 'O':
                array.append((0, j))
            if board[h - 1][j] == 'O':
                array.append((h - 1, j))
        while array:
            x, y = array.popleft()
            board[x][y] = 'A'
            for xx, yy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                if 0 <= xx < h and 0 <= yy < w and board[xx][yy] == 'O':
                    array.append((xx, yy))
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'

