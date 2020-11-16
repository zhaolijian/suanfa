# x的平方根
# 方法1
class Solution:
    def mySqrt(self, x: int) -> int:
        temp = 0
        while temp * temp <= x:
            temp += 1
        return temp - 1


# 方法2 二叉查找
class Solution:
    def mySqrt(self, x: int) -> int:
        end = x
        start = 0
        res = -1
        while start <= end:
            mid = (start + end) // 2
            if mid * mid <= x:
                res = mid
                start = mid + 1
            else:
                end = mid - 1
        return res


# 方法3 pow(x, 0.5) = pow(e, 0.5 * lnx)
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        temp = int(math.exp(0.5 * math.log(x)))
        return temp + 1 if (temp + 1) * (temp + 1) <= x else temp


if __name__ == '__main__':
    s = Solution()
    for i in range(100):
        print(s.mySqrt(i))