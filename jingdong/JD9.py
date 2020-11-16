class Solution:
    def function(self, n, m):
        res = 0
        while n:
            res += n % m
            n //= m
        return res

    def func(self, n):
        res = 0
        for i in range(1, n + 1):
            if self.function(i, 2) == self.function(i, 10):
                res += 1
        return res


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            s = Solution()
            print(s.func(n))
        except:
            break