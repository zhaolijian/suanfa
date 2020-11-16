class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0
        res = 0
        init = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix[0])):
            init[0][i] = int(matrix[0][i])
            if init[0][i] > res:
                res = init[0][i]
        for i in range(len(matrix)):
            init[i][0] = int(matrix[i][0])
            if init[i][0] > res:
                res = init[i][0]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if int(matrix[i][j]) == 0:
                    init[i][j] = 0
                else:
                    init[i][j] = min(init[i-1][j], init[i][j-1], init[i-1][j-1]) + 1
                    if init[i][j] > res:
                        res = init[i][j]
        return pow(res, 2)


if __name__ == '__main__':
    s = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # matrix = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
    # matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    print(s.maximalSquare(matrix))