# 方法1 dp
class Solution:
    def maximalSquare(self, matrix) -> int:
        res, heigth, width = 0, len(matrix), len(matrix[0])
        init = [[0 for i in range(width)] for j in range(heigth)]
        for i in range(width):
            init[0][i] = int(matrix[0][i])
            if init[0][i] > res:
                res = init[0][i]
        for i in range(heigth):
            init[i][0] = int(matrix[i][0])
            if init[i][0] > res:
                res = init[i][0]
        for i in range(1, heigth):
            for j in range(1, width):
                if int(matrix[i][j]) == 0:
                    init[i][j] = 0
                else:
                    init[i][j] = min(init[i-1][j], init[i][j-1], init[i-1][j-1]) + 1
                    if init[i][j] > res:
                        res = init[i][j]
        return pow(res, 2)


# 方法2 栈
class Solution:
    def maximalSquare(self, matrix) -> int:
        height, width = len(matrix), len(matrix[0])
        init = []
        first = []
        for i in range(width):
            first += [1] if matrix[0][i] == "1" else [0]
        init.append(first)
        for i in range(1, height):
            temp = []
            for j in range(width):
                if matrix[i][j] == "1":
                    temp.append(init[-1][j] + 1)
                else:
                    temp.append(0)
            init.append(temp)
        res = 0
        for i in range(height):
            stack = [-1]
            for j in range(width):
                while stack[-1] != -1 and init[i][stack[-1]] > init[i][j]:
                    val = min(init[i][stack.pop()], j - stack[-1] - 1)
                    res = max(res, val * val)
                stack.append(j)
            while stack[-1] != -1:
                val = min(init[i][stack.pop()], width - stack[-1] - 1)
                res = max(res, val * val)
        return res


if __name__ == '__main__':
    s = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # matrix = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
    # matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    print(s.maximalSquare(matrix))