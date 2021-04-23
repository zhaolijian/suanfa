# 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
# 给你网格图的行数 n 。
# 请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。

# 递推
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        # ABC型(比如012 021 102 120 201 210), ABA型(比如010 020 101 121 202 212)
        fi0, fi1 = 6, 6
        for i in range(1, n):
            # 下一行是ABC型,上一行也是ABC型(比如下一行为012, 则上一行可以是120、201,有两种)
            # 下一行是ABC型,上一行是ABA型(比如下一行为012, 则上一行可以是101、121,有两种)
            # 下一行是ABA型,上一行是ABC型(比如下一行为010, 则上一行可以是102、201,有两种)
            # 下一行是ABA型,上一行是ABA型(比如下一行为010, 则上一行可以是101、121、202,有三种)
            fi0, fi1 = (2 * fi0 + 2 * fi1) % mod, (2 * fi0 + 3 * fi1) % mod
        return (fi0 + fi1) % mod


# dfs超时
class Solution:
    def numOfWays(self, n: int) -> int:
        def dfs(i, j, color, init):
            if i == n - 1 and j == 2:
                return 1
            number = 0
            # 下一个节点可以使用的颜色
            for c in range(3):
                # 第一行,只需要和左侧颜色不同即可
                if i == 0:
                    # 当(i,j)不是第一行最后一个节点时
                    if j < 2:
                        if c != color:
                            init[i][j + 1] = c
                            number += dfs(i, j + 1, c, init)
                    # 当(i,j)是第一行最后一个节点时
                    else:
                        if i < n - 1 and c != init[i][0]:
                            init[i + 1][0] = c
                            number += dfs(i + 1, 0, c, init)
                # 不是第一行
                else:
                    # 当(i,j)不是该行最后一个节点时
                    if j < 2:
                        if c != color and c != init[i - 1][j + 1]:
                            init[i][j + 1] = c
                            number += dfs(i, j + 1, c, init)
                    else:
                        if i < n - 1 and c != init[i][0]:
                            init[i + 1][0] = c
                            number += dfs(i + 1, 0, c, init)
            return number

        init = [[-1] * 3 for i in range(n)]
        init[0][0] = 0
        return (dfs(0, 0, 0, init) * 3) % (pow(10, 9) + 7)