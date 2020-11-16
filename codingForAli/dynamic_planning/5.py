# 买卖股票问题：一个数组表示股票价格,总共只能进行一次交易


def solution(l):
    if len(l) <= 1:
        return 0
    maxProfit = 0
    curMin = l[0]
    # 比较当前值和之前的最小值差值、maxProfit
    for i in range(1, len(l)):
        if l[i] < curMin:
            curMin = l[i]
        maxProfit = max(maxProfit, l[i] - curMin)
    return maxProfit


if __name__ == '__main__':
    l = list(map(int, input().strip().split()))
    print(solution(l))


