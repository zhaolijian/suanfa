# 股票问题，只允许进行2次股票交易。这样可以以某个时间点为分割线，选择该时间点之前的最大利润+时间点之后的最大利润，
# 再从所有的时间点中选择最大利润


def solution(l):
    if len(l) <= 1:
        return 0
    else:
        # 存放每个时间点的最大利润
        result = []
        for i in range(1, len(l)):
            # 将该时间点及之前的分为一组、之后的分为一组
            left_profit = best(l[:i+1])
            right_profit = best(l[i+1:])
            result.append(left_profit+right_profit)
    return max(result)


def best(l):
    if len(l) <= 1:
        return 0
    else:
        min_value = l[0]
        profit = 0
        for i in range(1, len(l)):
            if l[i] < min_value:
                min_value = l[i]
            profit = max(profit, l[i] - min_value)
        return profit


if __name__ == '__main__':
    l = list(map(int, input().strip().split()))
    print(solution(l))
