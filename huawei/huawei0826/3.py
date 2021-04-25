# 5
# 5
# cloxy 3 0
# cxmnu 1 1
# kcotd 2 1
# apqud 2 0
# bldwz 1 1
# 总数组、已经找到的
def dfs(array, already, P, N):
    if not array and len(already) == P:
        return already
    for i in range(N):
        if int(array[i][1]) == P:
            return array[i]
    return 'cloud'


if __name__ == '__main__':
    while True:
        try:
            # 单词长度
            P = int(input())
            N = int(input())
            res = ""
            array = []
            for i in range(N):
                temp = input().split()
                array.append(temp)
            already = [None] * P
            print(dfs(array, already, P, N))
        except:
            break

