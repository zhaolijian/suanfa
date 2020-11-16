# 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）
if __name__ == '__main__':
    while True:
        try:
            s = input()
            length = len(s)
            res = 0
            d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
            for i in range(length - 1, 1, -1):
                if s[i] in d:
                    res += d[s[i]] * pow(16, length - i - 1)
                else:
                    res += int(s[i]) * pow(16, length - i - 1)
            print(str(res))

        except:
            break