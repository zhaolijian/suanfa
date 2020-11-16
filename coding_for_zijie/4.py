# 10个小球，随机分到12个盒子里，求恰好10个盒子都为空的概率。要求用Python程序模拟十万次
from random import randint
if __name__ == '__main__':
    number_balls = int(input())
    boxes = int(input())
    res = 0
    for i in range(1000000):
        temp = 0
        init = [0 for i in range(boxes)]
        for j in range(number_balls):
            number = randint(1, boxes)
            init[number - 1] += 1
        for i in range(boxes):
            if init[i] != 0:
                temp += 1
        if temp == 2:
            res += 1
    print(res / 1000000)