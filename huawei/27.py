# 先输入字典中单词的个数，再输入n个单词作为字典单词。
# 输入一个单词，查找其在字典中兄弟单词的个数
# 再输入数字n
if __name__ == '__main__':
    while True:
        try:
            l = list(input().split())
            number = int(l[0])
            array = l[1: number + 1]
            cur = l[-2]
            index = int(l[-1])
            res = 0
            temp = []
            for i in range(number):
                if array[i] != cur and sorted(array[i]) == sorted(cur):
                    res += 1
                    temp.append(array[i])
            print(res)
            if index <= len(temp):
                print(sorted(temp)[index - 1])
        except:
            break