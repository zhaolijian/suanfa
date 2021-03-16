# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        top, buttom, left, right = 0, m - 1, 0, n - 1
        res = []
        while top <= buttom and left <= right:
            res += matrix[top][left: right + 1]
            for i in range(top + 1, buttom + 1):
                res.append(matrix[i][right])
            if top < buttom:
                res += matrix[buttom][left: right][::-1]
            if left < right:
                for j in range(buttom - 1, top, -1):
                    res.append(matrix[j][left])
            top += 1
            buttom -=1
            left += 1
            right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [[7],[9],[6]]
    print(s.spiralOrder(matrix))