# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


class Solution:
    def rotate(self, matrix) -> None:
        length = len(matrix)
        if length <= 1:
            return
        top, botton, left, right = 0, length - 1, 0, length - 1
        while top < botton and left < right:
            temp = matrix[top].copy()
            for i in range(top, botton):
                matrix[top][length - 1 - i] = matrix[i][left]
            for i in range(left, right):
                matrix[i][left] = matrix[botton][i]
            for i in range(top + 1, botton + 1):
                matrix[botton][length - 1 - i] = matrix[i][right]
                matrix[i][right] = temp[i]
            top += 1
            botton -= 1
            left += 1
            right -= 1


# 方法2 水平翻转+对角线翻转
# class Solution:
#     def rotate(self, matrix) -> None:
#         length = len(matrix)
#         if length <= 1:
#             return
#         for i in range(length // 2):
#             for j in range(length):
#                 matrix[i][j], matrix[length - 1 - i][j] = matrix[length - 1 - i][j], matrix[i][j]
#         for i in range(length):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# 思路和方法1类似
# class Solution:
#     def rotate(self, matrix) -> None:
#         height = len(matrix)
#         if height <= 1:
#             return
#         number = (height + 1) // 2
#         for i in range(number):
#             temp = matrix[i][i: height - i]
#             for j in range(i, height-i):
#                 matrix[i][height-j-1] = matrix[j][i]
#             for j in range(i, height-i):
#                 matrix[j][i] = matrix[height-i-1][j]
#             for j in range(i, height-i):
#                 matrix[height-i-1][j] = matrix[height-j-1][height-i-1]
#             for j in range(len(temp)-1, -1, -1):
#                 matrix[i+j][height-i-1] = temp[j]


if __name__ == '__main__':
    s = Solution()
    matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.rotate(matrix))