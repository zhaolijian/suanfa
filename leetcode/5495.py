# 给你一个整数 n 和一个整数数组 rounds 。有一条圆形赛道由 n 个扇区组成，扇区编号从 1 到 n 。
# 现将在这条赛道上举办一场马拉松比赛，该马拉松全程由 m 个阶段组成。
# 其中，第 i 个阶段将会从扇区 rounds[i - 1] 开始，到扇区 rounds[i] 结束。
# 举例来说，第 1 阶段从 rounds[0] 开始，到 rounds[1] 结束。
# 请你以数组形式返回经过次数最多的扇区，按扇区编号 升序 排列。
# 注意，赛道按扇区编号升序逆时针形成一个圆（请参见第一个示例）。

# n = 4, rounds = [1,3,1,2]
# [1,2]

class Solution:
    def mostVisited(self, n: int, rounds):
        init = [0] * n
        init[rounds[0] - 1] += 1
        res = []
        for i in range(1, len(rounds)):
            if rounds[i] > rounds[i - 1]:
                for j in range(rounds[i - 1], rounds[i]):
                    init[j] += 1
            else:
                for j in range(rounds[i - 1], n):
                    init[j] += 1
                for j in range(rounds[i]):
                    init[j] += 1
        max_val = max(init)
        for i in range(n):
            if init[i] == max_val:
                res.append(i + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    n = 7
    rounds = [1,3,5,7]
    print(s.mostVisited(n, rounds))