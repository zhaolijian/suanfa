# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
# 一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


# 方法1 dfs+剪枝
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j):
            nonlocal res
            if not 0 <= i < m or not 0 <= j < n:
                return
            if init[i][j] == True:
                return
            if self.func(i) + self.func(j) > k:
                return
            res += 1
            init[i][j] = True
            dfs(i + 1, j)
            dfs(i, j + 1)

        init = [[False for i in range(n)] for j in range(m)]
        res = 0
        dfs(0, 0)
        return res

    def func(self, number):
        res = 0
        while number:
            res += number % 10
            number //= 10
        return res


# bfs+剪枝
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        q = [(0, 0)]
        s = set()
        while q:
            x, y = q.pop(0)
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and self.func(x) + self.func(y) <= k:
                s.add((x, y))
                q.append((x + 1, y))
                q.append((x, y + 1))
        return len(s)


    def func(self, number):
        res = 0
        while number:
            res += number % 10
            number //= 10
        return res


