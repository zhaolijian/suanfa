# 网格地下城游戏
# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        h, w = len(dungeon), len(dungeon[0])
        # 刚进入每一个网格时的最小值
        dp = [[0 for i in range(w)] for j in range(h)]
        dp[-1][-1] = 1 - dungeon[-1][-1] if dungeon[-1][-1] < 0 else 1
        for i in range(h - 2, -1, -1):
            # temp表示刚进入该表格的值
            temp = dp[i + 1][-1] - dungeon[i][-1]
            # 如果刚进入该表格值大于0，则为temp，否则为1
            dp[i][-1] = temp if temp > 0 else 1
        for j in range(w - 2, -1, -1):
            temp = dp[-1][j + 1] - dungeon[-1][j]
            dp[-1][j] = temp if temp > 0 else 1
        for i in range(h - 2, -1, -1):
            for j in range(w - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]), 1)
        return dp[0][0]


if __name__ == '__main__':
    s = Solution()
    dungeon = [[0,-3]]
    print(s.calculateMinimumHP(dungeon))