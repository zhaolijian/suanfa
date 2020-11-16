# 题目描述
# 小包最近迷上了一款叫做雀魂的麻将游戏，但是这个游戏规则太复杂，小包玩了几个月了还是输多赢少。
# 于是生气的小包根据游戏简化了一下规则发明了一种新的麻将，只留下一种花色，并且去除了一些特殊和牌方式（例如七对子等），具体的规则如下：
#
# 总共有36张牌，每张牌是1~9。每个数字4张牌。
# 你手里有其中的14张牌，如果这14张牌满足如下条件，即算作和牌
# 14张牌中有2张相同数字的牌，称为雀头。
# 除去上述2张牌，剩下12张牌可以组成4个顺子或刻子。顺子的意思是递增的连续3个数字牌（例如234,567等），刻子的意思是相同数字的3个数字牌（例如111,777）
#
# 例如：
# 1 1 1 2 2 2 6 6 6 7 7 7 9 9 可以组成1,2,6,7的4个刻子和9的雀头，可以和牌
# 1 1 1 1 2 2 3 3 5 6 7 7 8 9 用1做雀头，组123,123,567,789的四个顺子，可以和牌
# 1 1 1 2 2 2 3 3 3 5 6 7 7 9 无论用1 2 3 7哪个做雀头，都无法组成和牌的条件。
#
# 现在，小包从36张牌中抽取了13张牌，他想知道在剩下的23张牌中，再取一张牌，取到哪几种数字牌可以和牌。
# 输入描述:
# 输入只有一行，包含13个数字，用空格分隔，每个数字在1~9之间，数据保证同种数字最多出现4次。
# 输出描述:
# 输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。若满足条件的有多种牌，请按从小到大的顺序输出。若没有满足条件的牌，请输出一个数字0


def success(array):
    if not array:
        return True
    head = array[0]
    # len(array) % 3说明雀头存在
    if array.count(head) >= 2 and len(array) % 3 and success(array[2:]):
        return True
    if array.count(head) >= 3 and success(array[3:]):
        return True
    if head + 1 in array and head + 2 in array:
        array.remove(head)
        array.remove(head + 1)
        array.remove(head + 2)
        if success(array):
            return True
        array.append(head)
        array.append(head + 1)
        array.append(head + 2)
        array.sort()
    return False


array = list(map(int, input().split()))
res = []
for i in range(1, 10):
    if array.count(i) <= 3 and success(sorted(array + [i])):
        res.append(i)
if not res:
    print(0)
else:
    print(' '.join(map(str, res)))