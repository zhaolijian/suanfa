# 输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
number = int(input())
res = 0
while number > 0:
    temp = 0
    while number >= pow(2, temp):
        temp += 1
    res += 1
    number -= pow(2, temp - 1)
print(res)