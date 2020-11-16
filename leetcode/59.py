# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
class Solution:
    def generateMatrix(self, n: int):
        res = [[0 for i in range(n)] for j in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        cur = 1
        while cur <= n * n:
            for i in range(left, right + 1):
                res[top][i] = cur
                cur += 1
            top += 1
            for i in range(top, bottom + 1):
                res[i][right] = cur
                cur += 1
            right -= 1
            for i in range(right, left - 1, -1):
                res[bottom][i] = cur
                cur += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                res[i][left] = cur
                cur += 1
            left += 1
        return res