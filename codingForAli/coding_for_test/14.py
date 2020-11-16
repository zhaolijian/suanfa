# 给定一个已排序的数组，删除重复项，使每个元素最多允许出现两次，并返回新的长度。
# 不要为另一个数组分配额外的空间，必须在常量内存中这样做。
# 设定两个指针，一个指向当前遍历值，一个指向处理后的最后一个值


def solution(l):
    j = 0
    sum = 0
    for i in range(1, len(l)):
        if l[i] == l[j]:
            sum += 1
            if sum < 2:
                l[j+1] = l[i]
                j += 1
        else:
            l[j+1] = l[i]
            j += 1
            sum = 0
    return j + 1, l


if __name__ == '__main__':
    l = list(map(int, input().split()))
    result = solution(l)
    print(result[0])
    print(result[1])


