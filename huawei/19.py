# 开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
# 处理：
# 1、 记录最多8条错误记录，循环记录（或者说最后只输出最后出现的八条错误记录），
# 对相同的错误记录（净文件名（保留最后16位）称和行号完全匹配）只记录一条，错误计数增加；
# 2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
# 3、 输入的文件可能带路径，记录文件名称不能带路径。


if __name__ == '__main__':
    title = []
    s = {}
    while True:
        try:
            temp = list(input().split())
            filename = list(temp[0].split('\\'))[-1]
            line = temp[1]
            if len(filename) > 16:
                filename = filename[-16:]
            if (filename, line) in s:
                s[(filename, line)] += 1
            else:
                # 这题意说的不清楚
                title.append((filename, line))
                s[filename, line] = 1
        except:
            break

    for ele in title[-8:]:
        print(ele[0], ele[1], s[ele])
