class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        res = []
        def func(i, j, path):
            if obstacleGrid[i][j] == 1:
                return
            elif i == h - 1 and j == w - 1:
                path += [[i, j]]
                res.append(path)
            else:
                if i + 1 < h and not res:
                    func(i + 1, j, path + [[i, j]])
                if j + 1 < w and not res:
                    func(i, j + 1, path + [[i, j]])
        func(0, 0, [])
        return res[0] if res else []