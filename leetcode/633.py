# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。


# 方法1
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if pow(c, 0.5) % 1 == 0:
            return True
        if pow(c / 2, 0.5) % 1 == 0:
            return True
        for i in range(1, int(pow(c, 0.5)) + 1):
            another = c - pow(i, 2)
            if pow(another, 0.5) % 1 == 0:
                return True
        return False


# 方法2 二分查找
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(pow(c, 0.5))
        while left <= right:
            sum = left * left + right * right
            if sum == c:
                return True
            elif sum > c:
                right -= 1
            else:
                left += 1
        return False