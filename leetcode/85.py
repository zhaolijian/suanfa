class Solution:
    def maximalRectangle(self, matrix) -> int:
        height = len(matrix)
        width = len(matrix[0])
        res = 0
        init = [[0 for i in range(width)] for j in range(height)]
        for i in range(width):
            if matrix[0][i] == "1":
                init[0][i] = 1
        for i in range(1, height):
            for j in range(width):
                if matrix[i][j] == '0':
                    continue
                else:
                    if matrix[i - 1][j] == '0':
                        init[i][j] = 1
                    else:
                        init[i][j] = 1 + init[i - 1][j]
        for i in range(height):
            stack = [-1]
            for j in range(width):
                while stack[-1] != -1 and init[i][j] <= init[i][stack[-1]]:
                    res = max(res, init[i][stack.pop()] * (j - stack[-1] - 1))
                stack.append(j)
            while stack[-1] != -1:
                res = max(res, init[i][stack.pop()] * (width - stack[-1] - 1))
        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(s.maximalRectangle(matrix))

























