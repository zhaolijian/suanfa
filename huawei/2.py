# 写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。


if __name__ == '__main__':
    s = input()
    c = input()
    if ord(c) < 97:
        c = chr(ord(c) + 32)
    number = 0
    for i in range(len(s)):
        temp = s[i]
        if ord(temp) < 97:
            temp = chr(ord(temp) + 32)
        if temp == c:
            number += 1
    print(number)