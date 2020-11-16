# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            temp = 3
            init = []
            init.extend([0, 1, 2])
            while temp <= number:
                init.append(init[temp-1] + init[temp-2])
                temp += 1
            return init[-1]


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        print(s.jumpFloor(i))
