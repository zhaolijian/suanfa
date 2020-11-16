# class Solution:
#     def bulbSwitch(self, n: int) -> int:
#         init = [0] * n
#         number = 0
#         # 每次更改的间隔
#         for i in range(1, n+1):
#             # 看看是不是更改间隔的整数倍
#             for j in range(1, n+1):
#                 if j % i == 0:
#                     if init[j-1] == 0:
#                         init[j - 1] = 1
#                     else:
#                         init[j-1] = 0
#         for index in range(n):
#             if init[index] == 1:
#                 number += 1
#         return number

import math


# 灯开关的变换只与是否有平方根有关，因为其他的因子会抵消
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


if __name__ == '__main__':
    s = Solution()
    print(s.bulbSwitch(3))