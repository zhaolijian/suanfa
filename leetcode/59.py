# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
class Solution:
    def generateMatrix(self, n: int):
        res = [[1 for i in range(n)] for j in range(n)]
        left, right, top, buttom = 0, n - 1, 0 , n - 1
        number = 1
        while left <= right and top <= buttom:
            for i in range(left, right + 1):
                res[top][i] = number
                number += 1
            for j in range(top + 1, buttom + 1):
                res[j][right] = number
                number += 1
            if top < buttom:
                for p in range(right - 1, left - 1, -1):
                    res[buttom][p] = number
                    number += 1
            if left < right:
                for q in range(buttom - 1, top , -1):
                    res[q][left] = number
                    number += 1
            left += 1
            right -= 1
            top += 1
            buttom -= 1
        return res


# 相同思路，不同写法
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