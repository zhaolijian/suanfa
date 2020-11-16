# 题目描述
# 原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
# 一个长整数。
# 举例：一个ip地址为10.0.3.193
# 每段数字             相对应的二进制数
# 10                   00001010
# 0                    00000000
# 3                    00000011
# 193                  11000001
# 组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，
# 即该IP地址转换后的数字就是它了。
# 的每段可以看成是一个0-255的整数，需要对IP地址进行校验
def toTen(string):
    l = string.split('.')
    res = int(l[-1])
    temp = 8
    for i in range(2, -1, -1):
        number = int(l[i])
        for j in range(8):
            if number & (1 << j):
                res += 1 << (temp + j)
        temp += 8
    return res


def toIp(string):
    res = []
    number = int(string)
    temp = ''
    init = 31
    while init >= 0:
        temp += '1' if number & (1 << init) else '0'
        init -= 1
    cur = 0
    for i in range(32):
        cur += int(temp[i]) << (7 - i % 8)
        if (i + 1) % 8 == 0:
            res.append(str(cur))
            cur = 0
    return '.'.join(res)


if __name__ == '__main__':
    while True:
        try:
            s1 = input()
            s2 = input()
            print(toTen(s1))
            print(toIp(s2))
        except:
            break