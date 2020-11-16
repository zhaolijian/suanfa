# 给定一个已排序的数组，删除重复项，使每个元素只出现一次，并返回新的长度。
# 不要为另一个数组分配额外的空间，必须在常量内存中这样做。
# 例如，给定输入数组A = [1,1,2]，
# 你的函数应该返回长度= 2,A现在是[1,2]。


def solution(l):
    # 已经排序好的最后一个索引
    j = 0
    for i in range(1, len(l)):
        if l[i] == l[j]:
            continue
        else:
            l[j+1] = l[i]
            j += 1
    return j+1


if __name__ == '__main__':
    l = list(map(int, input().split()))
    print(solution(l))

