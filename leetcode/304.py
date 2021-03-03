# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。

# 方法1 图形面积变换
class NumMatrix:
    def __init__(self, matrix):
        height, width = 0, 0
        if matrix and matrix[0]:
            height, width = len(matrix), len(matrix[0])
        self.new_matrix = [[0 for i in range(width + 1)] for j in range(height + 1)]
        for i in range(height):
            for j in range(width):
                self.new_matrix[i + 1][j + 1] = self.new_matrix[i][j + 1] + self.new_matrix[i + 1][j] - self.new_matrix[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.new_matrix[row2 + 1][col2 + 1] - self.new_matrix[row2 + 1][col1] - self.new_matrix[row1][col2 + 1] + self.new_matrix[row1][col1]


# 方法2 累加和+哈希表+图形面积变换
class NumMatrix:
    def __init__(self, matrix):
        height, width = 0, 0
        if matrix and matrix[0]:
            height, width = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.dict = {}
        for i in range(height + 1):
            self.dict[(i, 0)] = 0
        for j in range(width + 1):
            self.dict[(0, j)] = 0
        # 每一行累加和
        for i in range(height):
            for j in range(1, width):
                self.matrix[i][j] += self.matrix[i][j - 1]
        for i in range(height):
            for j in range(width):
                self.dict[(i + 1, j + 1)] = self.dict[(i, j + 1)] + self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dict[(row2 + 1, col2 + 1)] - self.dict[(row2 + 1, col1)] - self.dict[(row1, col2 + 1)] + self.dict[(row1, col1)]


if __name__ == '__main__':
    s = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(s.sumRegion(2, 1, 4, 3))
    print(s.sumRegion(1, 1, 2, 2))
    print(s.sumRegion(1, 2, 2, 4))
