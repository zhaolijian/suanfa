# 插入排序


def solution(l):
    for i in range(1, len(l)):
        # 要插入值
        key = l[i]
        # 已经排序好的数组最后一个值
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        l = list(map(int, input().strip().split()))
        # 第一个数是个数
        result = solution(l[1:])
        print(" ".join(map(str, result)))

