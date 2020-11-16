# 给定n个字符串，请对n个字符串按照字典序排列。
number = int(input())
array = []
for _ in range(number):
    array.append(input())
array.sort()
for i in range(number):
    print(array[i])