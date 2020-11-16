# 给定一个数，求它至少需要多少个完全平方数想加得到（1，4，9。。。）


def solution(n):
    init = [n for i in range(n+1)]
    init[0] = 0
    for i in range(n+1):
        j = 1
        while i + j * j <= n:
            init[i + j * j] = min(init[i + j * j], init[i] + 1)
            j += 1
    return init[-1]


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
