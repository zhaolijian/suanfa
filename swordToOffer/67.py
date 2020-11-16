class Solution:
    def cutRope(self, number):
        m = 2
        res = 0
        while m <= number:
            if self.func(number, m) > res:
                res = self.func(number, m)
            m += 1
        return res

    # n长度，分为m段
    def func(self, n, m):
        number = 1
        for i in range(m):
            if n % (m - i) == 0:
                for j in range(m - i):
                    number *= (n // (m - i))
                break
            else:
                number *= (n // m + 1)
                n -= (n // m + 1)
        return number


if __name__ == '__main__':
    n = 2
    s = Solution()
    print(s.cutRope(n))
