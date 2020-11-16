# 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。
# 一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。
# 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。
# 主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。


class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        # 记录每一行最后一个1出现的位置
        init = [0] * n
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    init[i] = j
        no_sort = init
        init = sorted(init)
        for i in range(n):
            if init[i] > i:
                return -1
        res = 0
        for i in range(n):
            if no_sort[i] <= i:
                continue
            else:
                temp = 0
                # 找到下一个满足条件的行
                for j in range(i, n):
                    if no_sort[j] > i:
                        temp += 1
                    else:
                        break
                # 交换
                for k in range(i + temp, i, -1):
                    no_sort[k], no_sort[k - 1] = no_sort[k - 1], no_sort[k]
                res += temp
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]]
    print(s.minSwaps(grid))