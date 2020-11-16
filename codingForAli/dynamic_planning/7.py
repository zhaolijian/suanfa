# 经典动态规划问题，方格路径问题


def solution(m, n):
    # 初始化m行n列矩阵
    init = [[0 for i in range(n)] for j in range(m)]
    for p in range(1, m):
        init[p][0] = 1
    for q in range(1, n):
        init[0][q] = 1
    for i in range(1, m):
        for j in range(1, n):
            init[i][j] = init[i-1][j] + init[i][j-1]
    return init[-1][-1]


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    print(solution(m, n))
