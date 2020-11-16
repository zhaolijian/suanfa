# 3.30
# 第一个，n个鸡场，初始每个有a[i]只鸡，每个鸡场每天增长k只，并且每天最多的那个鸡场，卖一半鸡（向下取整），问m天后共几只鸡。


# 鸡场数、鸡场中鸡的个数列表、每天增长数k，m天后剩下的鸡数
def solution(n, l, k, m):
    while m > 0:
        # 哪个鸡场中的数量最大
        max_index = -1
        max_number = l[0]
        for i in range(n):
            if l[i] > max_number:
                max_index = i
                max_number = l[i]
            l[i] += k
        l[max_index] = l[max_index] // 2
        m -= 1
    return sum(l)


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().strip().split()))
    k = int(input())
    m = int(input())
    result = solution(n, l, k, m)
    print(result)