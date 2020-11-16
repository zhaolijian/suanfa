# -*- coding:utf-8 -*-
# 方法1，最优解
# class Solution:
#     def NumberOf1(self, n):
#         number = 0
#         n = n & 0xffffffff
#         while n != 0:
#             number += 1
#             n = n & (n-1)
#         return number


# 方法2， number右移。
class Solution:
    def NumberOf1(self, n):
        count = 0
        number = n & 0xffffffff
        one = 1
        while number:
            if number & one != 0:
                count += 1
            number >>= 1
        return count


if __name__ == '__main__':
    s = Solution()
    for i in range(-5, 5):
        print(s.NumberOf1(i))
