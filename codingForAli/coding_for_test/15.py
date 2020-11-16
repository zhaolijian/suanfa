# 在一个旋转的数组中找最小值,数组中元素无重复


# 使用二分法
def solution(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return min(l)
    else:
        start = 0
        end = len(l) - 1
        while start < end:
            if l[start] < l[end]:
                return l[start]
            mid = start + (end - start) // 2
            if l[mid] > l[start]:
                start = mid + 1
            elif l[mid] < l[start]:
                end = mid - 1
        return l[start]


if __name__ == '__main__':
    l = list(map(int, input().split()))
    print(solution(l))
