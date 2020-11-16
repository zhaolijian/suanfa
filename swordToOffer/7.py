# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            temp = 2
            init = []
            init.extend([0, 1])
            while temp <= n:
                init.append(init[temp-1]+init[temp-2])
                temp += 1
            return init[-1]


if __name__ == '__main__':
    s = Solution()
    for i in range(39):
        print(s.Fibonacci(i))
