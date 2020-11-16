# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        h, w = len(matrix), len(matrix[0])
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        for x, y in zeros:
            for i in range(h):
                matrix[i][y] = 0
            for j in range(w):
                matrix[x][j] = 0