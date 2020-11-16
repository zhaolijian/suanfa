# 在一个旋转的数组中找最小值,数组中元素可能有重复


# 使用二分法
def solution(l):
    if len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return min(l[0], l[1])
    else:
        start = 0
        end = len(l) - 1
        while start < end:
            if l[start] < l[end]:
                return l[start]
            mid = (start + end) // 2
            # 如果中间数大于开始数，则最小值应该在中间数右边
            if l[mid] > l[start]:
                start = mid + 1
            # 如果中间数小于开始数，那么最小值可能在mid处，也可能在它右边
            elif l[mid] < l[start]:
                end = mid
            # 如果相等，不确定在左边还是右边，start值后移
            elif l[mid] == l[start]:
                start += 1
        return l[start]


if __name__ == '__main__':
    l = list(map(int, input().split()))
    print(solution(l))
