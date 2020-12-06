# 给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        height, width = len(matrix), len(matrix[0])
        i, j = height - 1, 0
        while i >= 0 and j < width:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False