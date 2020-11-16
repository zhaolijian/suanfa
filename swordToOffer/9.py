# -*- coding:utf-8 -*-


# 1 1  2 2  3 4  4 1+1+2+1+3=8
class Solution:
    def jumpFloorII(self, number):
        return pow(2, number-1)


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(s.jumpFloorII(i))
