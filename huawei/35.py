# 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
# 样例输入
# 5
# 样例输出
# 1 3 6 10 15
# 2 5 9 14
# 4 8 13
# 7 12
# 11
def GetResult(n):
    init = [[0 for i in range(n)] for j in range(n)]
    init[0][0] = 1
    temp = 1
    for i in range(1, n):
        init[i][0] = init[i - 1][0] + temp
        temp += 1
    for i in range(n):
        temp = i + 2
        for j in range(1, n - i):
            init[i][j] = init[i][j - 1] + temp
            temp += 1
    return init


if __name__ == "__main__":
    while True:
        try:
            N = int(input())
            result = GetResult(N)
            for i in range(N):
                temp = result[i][:N - i]
                print(' '.join(map(str, temp)))
        except:
            break