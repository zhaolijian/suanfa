# 10个小球，随机分到12个盒子里，求恰好10个盒子都有球的概率。要求用Python程序模拟十万次
from random import randint
if __name__ == '__main__':
    number_balls = int(input())
    boxes = int(input())
    res = 0
    for i in range(100000):
        temp = 0
        init = [0 for i in range(12)]
        for j in range(12):
            number = randint(1, 12)
            init[number - 1] += 1
        for i in range(12):
            if init[i] == 1:
                temp += 1
        if temp == 10:
            res += 1
    print(res / 100000)