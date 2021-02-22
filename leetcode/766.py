# 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
# 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是托普利茨矩阵 。

# 方法1，每个元素只和左上角的元素比较即可
class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        height, width = len(matrix), len(matrix[0])
        for i in range(1, height):
            for j in range(1, width):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


# 方法2， 左上到右下看成一组，比较这一组元素值是否一样
class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        height, width = len(matrix), len(matrix[0])
        x, y = height - 1, 0
        for i in range(height + width - 1):
            init = matrix[x][y]
            plus = 1
            while x + plus < height and y + plus < width:
                if init != matrix[x + plus][y + plus]:
                    return False
                plus += 1
            if x > 0:
                x -= 1
            else:
                y += 1
        return True