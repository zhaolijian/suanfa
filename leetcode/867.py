# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

class Solution:
    def transpose(self, matrix):
        height, width = len(matrix), len(matrix[0])
        res = []
        for i in range(width):
            temp = []
            for j in range(height):
                temp.append(matrix[j][i])
            res.append(temp)
        return res
