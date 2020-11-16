# N皇后问题是指在N*N的棋盘上要摆N个皇后，要求任何两个皇后不同行，不同列也不再同一条斜线上，求给一个整数n，返回n皇后的摆法。
class Solution:
    def __init__(self):
        self.res = 0

    def Nqueen(self ,n):
        # 列数set集、左斜线set集(列-行范围为[-n,n])、右斜线set集(行+列范围为[0,2n])
        tb, l, r = set(), set(), set()
        def func(row):
            if row == n:
                self.res += 1
            for i in range(n):
                if i not in tb:
                    if (i - row) not in l and (i + row) not in r:
                        l.add(i - row)
                        r.add(i + row)
                        tb.add(i)
                        func(row + 1)
                        l.remove(i - row)
                        r.remove(i + row)
                        tb.remove(i)
        func(0)
        return self.res


if __name__ == '__main__':
    s = Solution()
    n = 8
    print(s.Nqueen(n))