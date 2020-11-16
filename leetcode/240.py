class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                col += 1
            else:
                row -= 1
        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(s.searchMatrix(matrix, target))