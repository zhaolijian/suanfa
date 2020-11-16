# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
number = float(input())
s = str(number)
index = -1
for i in range(len(s)):
    if s[i] == '.':
        index = i
        break
res = int(s[:index]) if int(s[index + 1]) < 5 else int(s[:index]) + 1
print(res)