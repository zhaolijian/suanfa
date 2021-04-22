# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。

# 方法1 有序集合
from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        height, width = len(matrix), len(matrix[0])
        res = float('-inf')
        for i in range(height):
            array = [0] * width
            for j in range(i, height):
                for p in range(width):
                    array[p] += matrix[j][p]
                s = SortedList([0])
                temp = 0
                for ele in array:
                    temp += ele
                    index = s.bisect_left(temp - k)
                    if index != len(s):
                        res = max(res, temp - s[index])
                    s.add(temp)
        return res

# 方法2 时间复杂度O(mmnn),找到上下两个边界的列和数组，然后通过两次for循环找到满足要求的结果
class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        height, width = len(matrix), len(matrix[0])
        res = float('-inf')
        for i in range(height):
            array = [0] * width
            for j in range(i, height):
                for m in range(width):
                    array[m] += matrix[j][m]
                for p in range(width):
                    temp = 0
                    for q in range(p, width):
                        temp += array[q]
                        if temp <= k and temp > res:
                            res = temp
        return res