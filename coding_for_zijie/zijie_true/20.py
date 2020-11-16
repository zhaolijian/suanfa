# 题目描述
# Z国的货币系统包含面值1元、4元、16元、64元共计4种硬币，以及面值1024元的纸币。现在小Y使用1024元的纸币购买了一件价值为N (0 < N \le 1024)N(0<N≤1024)的商品，请问最少他会收到多少硬币？
# 输入描述:
# 一行，包含一个数N。
# 输出描述:
# 一行，包含一个数，表示最少收到的硬币数。
N = int(input())
number = 1024 - N
res = 0
res += number // 64
number %= 64
res += number // 16
number %= 16
res += number // 4
number %= 4
res += number
print(res)