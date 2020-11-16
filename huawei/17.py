# 开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
# 从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
if __name__ == '__main__':
    while True:
        try:
            array = list(input().strip().split(';'))
            x, y = 0, 0
            s = {'A':(-1, 0), 'S':(0, -1), 'W':(0, 1), 'D': (1, 0)}
            for i in range(len(array)):
                length = len(array[i])
                if (length == 2 or length == 3) and array[i][0] in s:
                    if length == 2 and '0' <= array[i][1] <= '9':
                        x += s[array[i][0]][0] * int(array[i][1])
                        y += s[array[i][0]][1] * int(array[i][1])
                    elif length == 3 and '0' <= array[i][1] <= '9' and '0' <= array[i][2] <= '9':
                        number = int(array[i][1:])
                        x += s[array[i][0]][0] * number
                        y += s[array[i][0]][1] * number
            print(str(x) + ',' + str(y))
        except:
            break