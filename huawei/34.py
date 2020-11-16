# Lily上课时使用字母数字图片教小朋友们学习英语单词，每次都需要把这些图片按照大小（ASCII码值从小到大）排列收好。
# 请大家给Lily帮忙，通过C语言解决。
if __name__ == '__main__':
    while True:
        try:
            s = input()
            length = len(s)
            res = ''
            init = sorted([ord(ele) for ele in s])
            for i in range(length):
                res += chr(init[i])
            print(res)
        except:
            break