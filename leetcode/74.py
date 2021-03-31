# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        heigth, width = len(matrix), len(matrix[0])
        i, j = heigth - 1, 0
        while i >= 0 and j < width:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False