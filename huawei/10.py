# 编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。
# 不在范围内的不作统计。多个相同的字符只计算一次
string = input()
s = set()
number = 0
for i in range(len(string)):
    if string[i] in s:
        continue
    number += 1
    s.add(string[i])
print(number)