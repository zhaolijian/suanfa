# 先把N的i到j位置为0,然后与M<<i相加
# 先把N的i到j位置为0,然后与M<<i相加
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        for temp in range(i, j + 1):
            if (N & (1 << temp)):
                N -= (1 << temp)
        N += (M << i)
        return N