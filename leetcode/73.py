# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。


# 方法1 set集合，时间复杂度O(mn),空间复杂度O(m+n)
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        # 获取0所在的位置对应的行和列
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        # 将该行和列的所有元素置为0
        for row in rows:
            for j in range(n):
                matrix[row][j] = 0
        for col in cols:
            for i in range(m):
                matrix[i][col] = 0


# 方法2 使用第一行和第一列记录置为0的列和行
class Solution:
    def setZeroes(self, matrix) -> None:
        m, n = len(matrix), len(matrix[0])
        # 第一行和第一列是否为0
        first_row = any(matrix[0][i] == 0 for i in range(n))
        first_col = any(matrix[j][0] == 0 for j in range(m))
        # 第一行和第一列用来记录该列和该行是否置为0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
        return matrix

# class Solution:
#     def setZeroes(self, matrix) -> None:
#         m, n = len(matrix), len(matrix[0])
#         flag_col0 = any(matrix[i][0] == 0 for i in range(m))
#         flag_row0 = any(matrix[0][j] == 0 for j in range(n))
#
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = matrix[0][j] = 0
#
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0
#
#         if flag_col0:
#             for i in range(m):
#                 matrix[i][0] = 0
#
#         if flag_row0:
#             for j in range(n):
#                 matrix[0][j] = 0
#
#         return matrix


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,1,2,3],[3,0,5,2],[1,3,1,5]]
    print(s.setZeroes(matrix))