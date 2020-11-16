# 对于以下数字
# a = 1.23456
# b = 2.355
# c = 3.5
# d = 2.5
# e = 3

# 先加一个很小的数，如果不加对于b=2.355，下面的方法都会有错误
a = 1.23456 + 0.00000001
b = 2.355 + 0.00000001
c = 3.5 + 0.00000001
d = 2.5 + 0.00000001
e = 3

# 方法1,输出的结果是字符串，可以赋值
# a = format(a, '.2f')
# b = format(b, '.2f')
# c = format(c, '.2f')
# d = format(d, '.2f')
# print(a)
# print(b)
# print(c)
# print(d)

# 方法2，可以直接输出，但是不能赋值
# print('%.2f' % a)
# print('%.2f' % b)
# print('%.2f' % c)
# print('%.2f' % d)

# 方法3,可以赋值，但是对于3.5、2.5、2.501这种本来就只有一位或者第二位小数为0的数,则会保留一位，对于整数，则会输出整数
a = round(a, 2)
b = round(b, 2)
c = round(c, 2)
d = round(d, 2)
e = round(e, 2)
print(a)
print(b)
print(c)
print(d)
print(e)