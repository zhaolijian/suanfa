# 给定一个由0和1组成的2维矩阵，返回该矩阵中最大的由1组成的正方形的面积
class Solution:
    def solve(self , matrix ):
        # write code here
        if not matrix or not matrix[0]:
            return 0
        res = 0
        h, w = len(matrix), len(matrix[0])
        dp = [[0 for i in range(w)] for j in range(h)]
        dp[0][0] = 1 if matrix[0][0] == 1 else 0
        for i in range(1, h):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        for j in range(1, w):
            if matrix[0][j] == '1':
                dp[0][j] = 1
        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] == '1':
                    temp = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    dp[i][j] = temp + 1
                    res = max(res, dp[i][j])
        return res * res


if __name__ == '__main__':
    s = Solution()
    # matrix = [[1,0,1,1,1,1,1,0,0,0],[1,0,1,1,1,0,0,0,0,0],[1,0,1,0,1,1,1,0,0,0],[1,1,0,1,1,1,1,0,1,0],[1,1,1,1,1,1,1,1,0,0],[1,0,1,1,1,1,1,1,1,0],[1,0,1,1,1,1,1,1,1,0],[1,0,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,0,0],[1,0,1,1,0,1,1,0,0,0]]
    matrix = [['1','1','1'],['1','1','1'],['1','1','1'],['1','1','1']]
    print(s.solve(matrix))