# 有障碍物的最多路径问题


def solution(l, m, n):
    # 初始化m行n列矩阵
    init = [[0 for i in range(n)] for j in range(m)]
    for p in range(1, m):
        # 有障碍物
        if l[p][0] == 1:
            for temp in range(p, m):
                init[temp][0] = 0
            break
        else:
            init[p][0] = 1
    for q in range(1, n):
        if l[0][q] == 1:
            for temp in range(q, n):
                init[0][temp] = 0
            break
        else:
            init[0][q] = 1
    for i in range(1, m):
        for j in range(1, n):
            if l[i][j] == 1:
                init[i][j] = 0
            else:
                init[i][j] = init[i-1][j] + init[i][j-1]
    return init[-1][-1]


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    input_array = []
    for i in range(m):
        l = list(map(int, input().split()))
        input_array.append(l)
    print(solution(input_array, m, n))
