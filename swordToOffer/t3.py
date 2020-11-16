class Solution:
    # 整数m，房间数n
    def solu(self, m, n):
        if m == 1:
            return 1
        # 找到第一个冲突的房间key，前面的无冲突数乘以pow(m, n-key-1)
        res = 0
        for i in range(n-1):
            if i == 0:
                res += m * pow(m, n - i - 2)
            else:
                res += m * pow(m - 1, i) * pow(m, n - i - 2)
        return res % 100003


if __name__ == '__main__':
    l = list(map(int, input().split()))
    m, n = l[0], l[1]
    s = Solution()
    print(s.solu(m, n))

