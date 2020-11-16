# -*- coding:utf-8 -*-

# 方法1
# class Solution:
#
#     def printMatrix(self, matrix):
#         res = []
#         while matrix:
#             res.extend(matrix.pop(0))
#             # 若矩阵有空行，则跳过
#             if matrix and matrix[0]:
#                 for row in matrix:
#                     res.append(row.pop())
#             if matrix:
#                 res.extend(matrix.pop()[::-1])
#             # 若矩阵有空行，则跳过
#             if matrix and matrix[0]:
#                 for row in matrix[::-1]:
#                     res.append(row.pop(0))
#         return res


# 方法2
# class Solution:
#
#     def printMatrix(self, matrix):
#         res = []
#         rows = len(matrix)
#         cols = len(matrix[0])
#         if rows == 0 and cols == 0:
#             return res
#         left, right, top, bottom = 0, cols-1, 0, rows-1
#         while left <= right and top <= bottom:
#             res.extend(matrix[top][left:right+1])
#             for i in range(top + 1, bottom + 1):
#                 res.append(matrix[i][right])
#             if top != bottom and left != right:
#                 res.extend(matrix[bottom][right-1:left:-1])
#                 res.append(matrix[bottom][left])
#             if left != right:
#                 for i in range(bottom-1, top, -1):
#                     res.append(matrix[i][left])
#             left += 1
#             right -= 1
#             top += 1
#             bottom -= 1
#         return res


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return []
        h = len(matrix)
        w = len(matrix[0])
        temp = 0
        res = []
        top, bottom, left, right = 0, h, 0, w
        while top < bottom and left < right:
            if temp % 4 == 0:
                res.extend(matrix[top][left:right])
                temp += 1
                top += 1
            elif temp % 4 == 1:
                for i in range(top, bottom):
                    res.append(matrix[i][right-1])
                temp += 1
                right -= 1
            elif temp % 4 == 2:
                res.extend(list(reversed(matrix[bottom-1][left:right])))
                temp += 1
                bottom -= 1
            else:
                for i in range(bottom - 1, top - 1, -1):
                    res.append(matrix[i][left])
                temp += 1
                left += 1
        return res


if __name__ == '__main__':
    s = Solution()
    init = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # init = [[1],[2],[3],[4],[5]]
    # init = [[1, 2],[3, 4]]
    # init = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    result = s.printMatrix(init)
    print(result)
