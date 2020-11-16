# 求按从小到大的顺序的第N个丑数(只包含质因子2、3和5)。
# 1 2 3 4 5 6 8 10 一个丑数等于另一个丑数*2或3或5


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return index
        res = [0 for i in range(index)]
        res[0] = 1
        p2, p3, p5 = 0, 0, 0
        for i in range(1, index):
            res[i] = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
            if res[i] % 2 == 0:
                p2 += 1
            if res[i] % 3 == 0:
                p3 += 1
            if res[i] % 5 == 0:
                p5 += 1
        return res[index - 1]


if __name__ == '__main__':
    s = Solution()
    m = int(input())
    for _ in range(m):
        n = int(input())
        print(s.GetUglyNumber_Solution(n))