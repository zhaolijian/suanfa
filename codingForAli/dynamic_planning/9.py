# 有路径权重的问题, 使得到达右下角位置权重最小


def solution(l, m, n):
    # 初始化m行n列矩阵
    init = [[0 for i in range(n)] for j in range(m)]
    init[0][0] = l[0][0]
    for p in range(1, m):
        init[p][0] = init[p-1][0] + l[p][0]
    for q in range(1, n):
        init[0][q] = init[0][q-1] + l[0][q]
    for i in range(1, m):
        for j in range(1, n):
            init[i][j] = min(init[i-1][j], init[i][j-1]) + l[i][j]
    return init[-1][-1]


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    input_array = []
    for i in range(m):
        l = list(map(int, input().split()))
        input_array.append(l)
    print(solution(input_array, m, n))
