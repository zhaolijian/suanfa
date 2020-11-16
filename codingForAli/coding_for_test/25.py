# 计数排序


def solution(l):
    result = [0] * len(l)
    max_value = max(l)
    # 该数组中存放小于等于每一个位置的元素个数
    init = [0] * (max_value + 1)
    for i in l:
        init[i] += 1
    for j in range(1, len(init)):
        init[j] += init[j - 1]
    for m in l:
        result[init[m] - 1] = m
        init[m] -= 1
    return result


if __name__ == '__main__':
    while True:
        try:
            l = list(map(int, input().strip().split()))
            if len(l) == 0:
                break
            result = solution(l[1:])
            print(" ".join(map(str, result)))
        except EOFError:
            break

