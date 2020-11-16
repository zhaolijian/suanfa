# 小度最近在研究一个棋盘游戏，游戏规则如下：
#
# 一个N*N的棋盘，每个格子里面填写有1、2、3、4这四个数字中的某一个。
#
# 最开始时在第1行第1列（左上角）放置一个棋子。每次棋子可以移动至上、下、左、右四个格子中的某一个，每次只能移动一格（允许重复移动到某一个格子），在任何时刻都不允许将棋子移出棋盘。
#
# 在移动时需要进行计分。如果初始格子中的数字为X，目标格子中的数字为Y，则本次移动计分为|X-Y|（取X-Y的绝对值），即两个格子中的数字之差。
#
# 现在需要把棋子移动到第N行第N列（右下角），请问能够获得的最小计分为多少？
#
#
#
# 输入描述
# 单组输入。
#
# 第1行为N。（1≤N≤100）
#
# 接下来N行为一个二维数组，表示棋盘上每一个格子及其对应的数字（正整数）。
#
# 输出描述
# 输出一个正整数，表示最小计分。

# 样例输入
# 3
# 1 2 4
# 1 3 1
# 1 2 1
# 样例输出
# 2


# if __name__ == '__main__':
#     N = int(input())
#     array = []
#     for _ in range(N):
#         array.append(list(map(int, input().split())))
#     dp = [[0 for i in range(N)] for j in range(N)]
#     for i in range(1, N):
#         dp[0][i] = dp[0][i - 1] + abs(array[0][i] - array[0][i - 1])
#     for j in range(1, N):
#         dp[j][0] = dp[j - 1][0] + abs(array[j][0] - array[j - 1][0])
#     for i in range(1, N):
#         for j in range(1, N):
#             dp[i][j] = min(dp[i - 1][j] + abs(array[i][j] - array[i - 1][j]), dp[i][j - 1] + abs(array[i][j] - array[i][j - 1]))
#     print(dp[-1][-1])
