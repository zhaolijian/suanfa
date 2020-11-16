# 兰博教训提莫之后,然后和提莫讨论起约德尔人,谈起约德尔人,自然少不了一个人,
# 那 就是黑默丁格------约德尔人历史上最伟大的科学家. 提莫说,黑默丁格最近在思考一个问题:
# 黑默丁格有三个炮台,炮台能攻击到距离它R的敌人 (两点之间的距离为两点连续的距离,例如(3,0),(0,4)之间的距离是5),
# 如果一个炮台能攻击 到敌人,那么就会对敌人造成1×的伤害.黑默丁格将三个炮台放在N*M方格中的点上,
# 并且给出敌人的坐标. 问:那么敌人受到伤害会是多大?
if __name__ == '__main__':
    while True:
        try:
            temp = list(map(int, input().split()))
            length = temp[0]
            array = temp[1:-2]
            x0, y0 = temp[-2], temp[-1]
            res = 0
            for i in range(0, len(array), 2):
                if pow(array[i] - x0, 2) + pow(array[i + 1] - y0, 2) <= length * length:
                    res += 1
            print(str(res) + 'x')
        except:
            break