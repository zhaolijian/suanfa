# 斐波那契数列
# dp[n] = dp[n - 1] + dp[n - 2]
# 初始条件dp[1] = 1, dp[2] = 2
# 总共有n个台阶，每次只能迈1阶或者2阶，问有多少中不同的方式


def solution(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return solution(n-1) + solution(n-2)


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
