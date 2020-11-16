# 计算字符串最后一个单词的长度，单词以空格隔开。
if __name__ == '__main__':
    s = list(input().strip().split())
    print(len(s[-1]))