# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
class Solution:
    def maximalRectangle(self, matrix) -> int:
        height = len(matrix)
        width = len(matrix[0])
        res = 0
        # 每个点上面连续1的个数，即连续1的宽度
        init = [[0 for i in range(width)] for j in range(height)]
        for i in range(width):
            if matrix[0][i] == "1":
                init[0][i] = 1
        for i in range(1, height):
            for j in range(width):
                if matrix[i][j] == '0':
                    continue
                else:
                    if matrix[i - 1][j] == '0':
                        init[i][j] = 1
                    else:
                        init[i][j] = 1 + init[i - 1][j]
        for i in range(height):
            stack = [-1]
            for j in range(width):
                while stack[-1] != -1 and init[i][j] <= init[i][stack[-1]]:
                    res = max(res, init[i][stack.pop()] * (j - stack[-1] - 1))
                stack.append(j)
            while stack[-1] != -1:
                res = max(res, init[i][stack.pop()] * (width - stack[-1] - 1))
        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(s.maximalRectangle(matrix))

























