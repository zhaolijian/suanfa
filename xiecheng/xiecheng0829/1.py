# 10
# MMATSATMMT
# 头部字符串满足至少包含一个“MT”子序列，且以T结尾。尾部字符串需要满足至少包含一个“MT”子序列，且以M开头
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            T = input().strip()
            # 使前后最短，则中间最长
            flag = False
            l, r = -1, -1
            for i in range(n):
                if T[i] == 'T' and flag:
                    l = i
                    break
                elif T[i] == 'M':
                    flag = True
            flag = False
            for j in range(n - 1, -1, -1):
                if T[j] == 'M' and flag:
                    r = j
                    break
                elif T[j] == 'T':
                    flag = True
            print(T[l + 1: r])
        except:
            break