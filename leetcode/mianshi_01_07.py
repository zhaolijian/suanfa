# 旋转矩阵90度
# 方法1 上下旋转再对角线翻折
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w = len(matrix)
        for i in range(w // 2):
            for j in range(w):
                # 题目中说不占用额外内存空间，其实在交换的时候要占用一个的
                matrix[i][j], matrix[w - i - 1][j] = matrix[w - i - 1][j], matrix[i][j]
        for i in range(1, w):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# 方法2 四个元素一个循环
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w = len(matrix)
        for i in range(w // 2):
            for j in range((w + 1) // 2):
                matrix[i][j], matrix[j][w - i - 1], matrix[w - i - 1][w - j - 1], matrix[w - j - 1][i] = matrix[w - j - 1][i], matrix[i][j], matrix[j][w - i - 1], matrix[w - i - 1][w - j - 1]


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.rotate(matrix))