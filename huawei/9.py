# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
number = int(input())
string = str(number)
s = set()
res = ''
for i in range(len(string) - 1, -1, -1):
    if string[i] in s:
        continue
    res += string[i]
    s.add(string[i])
print(int(res))