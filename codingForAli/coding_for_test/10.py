import collections
# 给定n个非负数选择中位数,使用分桶排序的思想


def solution(l):
    l.sort()
    max_value = max(l)
    num = 0
    init = [0 for i in range(max_value + 1)]
    for temp in l:
        init[temp] += 1
    for j in range(max_value + 1):
        num += init[j]
        # 如果总数为偶数
        if len(l) % 2 == 0:
            if num == len(l) / 2:
                for k in range(j + 1, max_value + 1):
                    if init[k] != 0:
                        return (j + k) / 2
            elif num > len(l) / 2:
                return j
        # 如果总数为奇数
        elif len(l) % 2 != 0 and num > (len(l) / 2):
            return j


if __name__ == '__main__':
    l = list(map(int, input().strip().split()))
    print(solution(l))


















