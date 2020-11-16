# 在一个排好序的有元素重复的数组中找到某个元素出现的范围，复杂度O(logn)


def solution(l, target):
    result = []
    start = 0
    end = len(l) - 1
    while start < end:
        mid = (start + end) // 2
        if l[mid] < target:
            start = mid + 1
        elif l[mid] >= target:
            end = mid
    # 重复元素开始位置
    result.append(start)
    ss = start
    ee = len(l) - 1
    while ss < ee:
        mid = (ss + ee) // 2
        if l[mid] > target:
            ee = mid - 1
        elif l[mid] == target:
            ss = mid
    result.append(ss)
    return result


if __name__ == '__main__':
    l = list(map(int, input().strip().split()))
    target = int(input())
    print(solution(l, target))