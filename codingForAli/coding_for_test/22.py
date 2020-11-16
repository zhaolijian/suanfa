# 按照数值出现个数排序，出现个数相同，按照值大小排序
import collections


def solution(l):
    result = []
    # 或者值、数量的键值对形式
    temp = collections.Counter(l)
    # 个数的负值、值的map
    map_array = [(-temp[i], i) for i in temp]
    map_array.sort()
    # 值、个数
    for key, val in map_array:
        result.extend([val]*(-key))
    return result


if __name__ == '__main__':
    l = list(map(int, input().split()))
    print(' '.join(map(str, solution(l))))
