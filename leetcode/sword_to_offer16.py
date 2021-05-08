# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        number = abs(n)
        temp = self.myPow(x, number // 2)
        if n < 0:
            if number % 2 == 0:
                return 1 / (temp * temp)
            return 1 / (temp * temp * x)
        if number % 2 == 0:
            return temp * temp
        return temp * temp * x