# •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
# 连续输入字符串(输入2次,每个字符串长度小于100)
if __name__ == '__main__':
    def func(s):
        length = len(s)
        if length == 0:
            print(s)
        elif length <= 8:
            print(s + (8 - length) * '0')
        else:
            temp = length // 8
            temp1 = length % 8
            for i in range(temp):
                print(s[i * 8: i * 8 + 8])
            if temp1:
                print(s[temp * 8:] + (8 - temp1) * '0')

    func(input())
    func(input())