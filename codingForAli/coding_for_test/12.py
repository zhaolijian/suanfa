# 在一个数组中移除制定数字，并将后面的往前移动，返回新的数组长度
def solution(l, target):
    j = 0
    for i in range(len(l)):
        if l[i] == target:
            continue
        else:
            l[j] = l[i]
            j += 1
    return j, l


if __name__ == '__main__':
    l = list(map(int, input().split()))
    target = int(input())
    result = solution(l, target)
    print(result[0])
    print(result[1])
