# 给你一个整数n,请你判断n是否为丑数。如果是，返回true；否则，返回false。丑数就是只包含质因数2、3和 / 或5的正整数。

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 5 == 0:
            n //= 5
        while n % 3 == 0:
            n //= 3
        while n % 2 == 0:
            n //= 2
        return n == 1