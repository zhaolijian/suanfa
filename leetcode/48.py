class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        if height <= 1:
            return matrix
        number = (height + 1) // 2
        for i in range(number):
            temp = matrix[i][i: height - i]
            for j in range(i, height-i):
                matrix[i][height-j-1] = matrix[j][i]
            for j in range(i, height-i):
                matrix[j][i] = matrix[height-i-1][j]
            for j in range(i, height-i):
                matrix[height-i-1][j] = matrix[height-j-1][height-i-1]
            for j in range(len(temp)-1, -1, -1):
                matrix[i+j][height-i-1] = temp[j]
        return matrix


if __name__ == '__main__':
    s = Solution()
    # matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.rotate(matrix))