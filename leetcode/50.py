# 二分法
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def func(number):
            if number == 0:
                return 1
            temp = func(number // 2)
            return temp * temp if number % 2 == 0 else temp * temp * x
        return func(n) if n >= 0 else 1 / func(-n)



if __name__ == '__main__':
    s = Solution()
    x = 2.0
    n = 10
    print(s.myPow(x, n))