# 买卖股票问题：一个数组表示股票价格,每天不限制交易次数。在低点买入高点卖出


def solution(l):
    if len(l) <= 1:
        return 0
    sum = 0
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            sum += (l[i] - l[i-1])
    return sum 


if __name__ == '__main__':
    l = list(map(int, input().strip().split()))
    print(solution(l))
