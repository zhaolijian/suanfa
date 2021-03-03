# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。


class Solution:
    def flipAndInvertImage(self, A):
        height, width = len(A), len(A[0])
        for i in range(height):
            left, right = 0, width - 1
            while left < right:
                if A[i][left] == A[i][right]:
                    A[i][left] ^= 1
                    A[i][right] ^= 1
                left += 1
                right -= 1
            if left == right:
                A[i][left] ^= 1
        return A


if __name__ == '__main__':
    s = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(s.flipAndInvertImage(A))