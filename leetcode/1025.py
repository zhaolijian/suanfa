# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
# 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
# 选出任一 x，满足 0 < x < N 且 N % x == 0 。
# 用 N - x 替换黑板上的数字 N 。
# 如果玩家无法执行这些操作，就会输掉游戏。
# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

# 方法1 数学方法
# N = 1时，。。。
# N = 2时。。。
# 假设N = k时成立，
# 则N = K + 1时，。。。
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


# 方法2 dp
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        dp = [False for i in range(N + 1)]
        dp[2] = True
        for i in range(3, N + 1):
            for j in range(1, i):
                # 如果i能够整除j，且dp[i - j]=False，则说明爱丽丝如果选择了j，则爱丽丝赢了
                if i % j == 0 and not dp[i - j]:
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    N = 1
    print(s.divisorGame(N))