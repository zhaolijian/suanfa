# 在一个排好序的数组中查找某个数，如果存在，返回下标，如果不存在，则返回应该插入的位置


def solution(l, target):
    start = 0
    end = len(l) - 1
    while start < end:
        mid = (start + end) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            end = mid
        elif l[mid] < target:
            start = mid + 1
    return start


if __name__ == '__main__':
    l = list(map(int, input().split()))
    target = int(input())
    print(solution(l, target))