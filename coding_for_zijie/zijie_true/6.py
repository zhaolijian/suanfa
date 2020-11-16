# 题目描述
# 有n个房间，现在i号房间里的人需要被重新分配，分配的规则是这样的：先让i号房间里的人全都出来，接下来按照 i+1, i+2, i+3, ... 的顺序依此往这些房间里放一个人，n号房间的的下一个房间是1号房间，直到所有的人都被重新分配。
# 现在告诉你分配完后每个房间的人数以及最后一个人被分配的房间号x，你需要求出分配前每个房间的人数。数据保证一定有解，若有多解输出任意一个解。
# 输入描述:
# 第一行两个整数n, x (2<=n<=10^5, 1<=x<=n)，代表房间房间数量以及最后一个人被分配的房间号；
# 第二行n个整数 a_i(0<=a_i<=10^9) ，代表每个房间分配后的人数。
# 输出描述:
# 输出n个整数，代表每个房间分配前的人数。


if __name__ == '__main__':
    # 房间数量、最后分配的房间号
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    # 循环次数
    number = min(array)
    for i in range(n):
        array[i] -= number
    res = n * number
    init = x - 1
    # 从最后分配的房间号处往前遍历，直到碰到有个位置为0，该位置就是起始位置
    while array[init]:
        res += 1
        array[init] -= 1
        init = (init - 1 + n) % n
    array[init] += res
    print(' '.join(map(str, array)))