# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
# 最后一个数后面也要有空格


# 方法1
x = int(input())
flag = False
for i in range(2, x // 2 + 1):
    while x % i == 0:
        flag = True
        print(i, end=' ')
        x = x // i
if not flag:
    print(x, end=' ')


# 方法2
x = int(input())
flag = False
for i in range(2, x + 1):
    while x % i == 0:
        flag = True
        print(i, end=' ')
        x = x // i


# 方法3
x = int(input())
p = 2
while True:
    if x % p == 0:
        print(p, end=' ')
        x //= p
    elif p * p > x:
        print(x, end=' ')
        break
    else:
        p += 1