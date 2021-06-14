# 顺指针打印矩阵

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        height, width = len(matrix), len(matrix[0])
        t, b, l, r = 0, height - 1, 0, width - 1
        res = []
        while t <= b and l <= r:
            res += matrix[t][l:r + 1]
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if r < l:
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if b < t:
                break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res