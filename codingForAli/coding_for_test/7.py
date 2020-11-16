# 给定一组数字，如何分组使他们差值最小
def solution(min_cap, max_cap, l):
    if min_cap == max_cap:
        return min_cap
    else:
        cap = (min_cap + max_cap) // 2
        num = sol(cap, l)
        # 说明桶大，足以满足,操作便是能不能让桶再小一点
        if num <= 2:
            return solution(min_cap, cap, l)
        else:
            return solution(cap+1, max_cap, l)


# 如果按照桶大小为cap分的话，需要几个桶,桶的大小在该题中为数字分成两组中较大那一组的数字之和
def sol(cap, l):
    # 数字之和
    sum = 0
    # 桶数
    number = 0
    if len(l) != 0:
        number = 1
    for i in l:
        sum += i
        if sum > cap:
            number += 1
            sum = i
    return number


if __name__ == '__main__':
    l = list(map(int, input().strip().split()))
    min_cap = min(l)
    max_cap = sum(l)
    result = solution(min_cap, max_cap, l)
    print(result)
