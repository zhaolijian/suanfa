# 求出一个三角形中从顶到底最小路径和，并且要求只能使用O(n)的空间。


# 从下往上，dp公式： init[i][j] = min(init[i+1][j], init[i+1][j+1]) + array[i][j]
def solution(m, n, array):
    if len(array) == 1:
        return array[0]
    for i in range(m-2, -1, -1):
        for j in range(i+1):
            array[i][j] = min(array[i+1][j], array[i+1][j+1]) + array[i][j]
    return array[0][0]


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    input_array = []
    for i in range(m):
        l = list(map(int, input().split()))
        input_array.append(l)
    print(solution(m, n, input_array))
