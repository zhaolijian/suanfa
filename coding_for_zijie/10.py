# 一辆巴士载了25人，路经10个车站。每个乘客以相同的概率在各个车站下车。如果某个车站有乘客要下车，则大巴在该站停车。
# 每个乘客下车的行为是独立的。记大巴停车次数为X，求X的数学期望（要求通过编程求数学期望）。
from random import randint
class Solution:
    def func(self, people, stations):
        init = [0] * stations
        for i in range(people):
            temp = randint(1, 10)
            init[temp - 1] += 1
        res = 0
        for i in init:
            if i != 0:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    numbers = int(input())
    people = int(input())
    stations = int(input())
    result = 0
    for _ in range(numbers):
        result += s.func(people, stations)
    print(result / numbers)