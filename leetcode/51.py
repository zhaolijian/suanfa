# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
class Solution:
    def solveNQueens(self, n: int):
        res = []
        result = []

        def func(row, array):
            if row == n:
                res.append(array)
                return
            for i in range(n):
                if i not in already and (i + row) not in l and (row - i) not in r:
                    l.add(i + row)
                    r.add(row - i)
                    already.add(i)
                    func(row + 1, array + [i])
                    l.remove(i + row)
                    r.remove(row - i)
                    already.remove(i)

        already = set()
        # 行下标+列下标=0...2n-2,用来确定是否处于同一斜线
        l = set()
        # 行下标-列下标=1-n...n-1,用来确定是否处于同一斜线
        r = set()
        # 已经存放的每行Q的位置
        func(0, [])

        for array in res:
            init = []
            for ele in array:
                temp = '.' * ele + 'Q' + '.' * (n - ele - 1)
                init.append(temp)
            result.append(init)
        return result


if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.solveNQueens(n))