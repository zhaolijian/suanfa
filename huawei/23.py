# 实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，
# 字符串中其它字符保持原来的顺序。
# 注意每个输入文件有多组输入，即多个字符串用回车隔开

if __name__ == '__main__':
    while True:
        try:
            s = input()
            length = len(s)
            res = ""
            d = {}
            for i in range(length):
                if s[i] in d:
                    d[s[i]] += 1
                else:
                    d[s[i]] = 1
            min_number = float('inf')
            for key in d.keys():
                if d[key] < min_number:
                    min_number = d[key]
            temp = set()
            for key in d.keys():
                if d[key] == min_number:
                    temp.add(key)
            for i in range(length):
                if s[i] not in temp:
                    res += s[i]
            print(res)
        except:
            break