# 给定一个整数矩阵，找出最长递增路径的长度。
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
class Solution:
    def __init__(self):
        self.res = 0

    def longestIncreasingPath(self, matrix) -> int:
        @lru_cache(None)
        def dfs(i, j):
            best = 1
            for p, q in init:
                result_x, result_y = i + p, j + q
                if 0 <= result_x < h and 0 <= result_y < w and matrix[result_x][result_y] > matrix[i][j]:
                    best = max(best, dfs(result_x, result_y) + 1)
            return best

        if not matrix or not matrix[0]:
            return 0
        h, w = len(matrix), len(matrix[0])
        init = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        for i in range(h):
            for j in range(w):
                res = max(res, dfs(i, j))
        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [[7,8,9],[9,7,6],[7,2,3]]
    print(s.longestIncreasingPath(matrix))