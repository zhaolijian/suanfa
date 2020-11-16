# 给定一个数n，求二叉树的排序方式数量，用来存储1...n
# 二叉树的左子树节点比根节点小，右子树节点比根节点大
# for i in range(n)
# 排序方式：dp[i] = dp[k] * dp[i-k-1]


def solution(n):
    init = [0 for i in range(n + 1)]
    init[0] = 1
    init[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            init[i] += init[j] * init[i-j-1]
    return init[-1]


if __name__ == '__main__':
    m = int(input())
    print(solution(m))

