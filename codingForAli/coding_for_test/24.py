# 冒泡排序


def solution(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


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

