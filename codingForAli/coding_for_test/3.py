# 阿里 3.25
# 给出一个数组，从每一列中选择一个数，求出后一列减去前一列的绝对值的和的最小值


# l为元祖列表
def solution(l):
    # 存储到该元素为止的满足条件的绝对值之和最小值
    init = []
    init.append([0, 0, 0])
    for i in range(1, len(l)):
        # 每行的绝对值之和最小值集合
        temp = []
        for j in range(3):
            cha = []
            cha.append(abs(l[i][j] - l[i - 1][0]) + init[i-1][0])
            cha.append(abs(l[i][j] - l[i - 1][1]) + init[i-1][1])
            cha.append(abs(l[i][j] - l[i - 1][2]) + init[i-1][2])
            temp.append(min(cha))
        init.append(temp)
    return min(init[-1])


if __name__ == '__main__':
    l1 = list(map(int, input().strip().split()))
    l2 = list(map(int, input().strip().split()))
    l3 = list(map(int, input().strip().split()))
    l = list(zip(l1, l2, l3))
    result = solution(l)
    print(result)
