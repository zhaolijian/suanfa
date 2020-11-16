# 求数组中的连乘最大值


def solution(l):
    result = 0
    if len(l) == 1:
        return l[0]
    else:
        init = [0 for i in range(len(l))]
        init[0] = l[0]
        # 遍历到当前节点之前的最小乘积
        min_last = l[0]
        # 遍历到当前节点之前的最大乘积
        max_last = l[0]
        for j in range(1, len(l)):
            temp = min_last
            min_last = min(min_last * l[j], l[j], max_last * l[j])
            max_last = max(max_last * l[j], l[j], temp * l[j])
            init[j] = max(max_last, l[j])
        return max(init)


if __name__ == '__main__':
    l = list(map(int, input().split()))
    print(solution(l))
