# 小团从某不知名论坛上突然得到了一个测试默契度的游戏，想和小美玩一次来检验两人的默契程度。
# 游戏规则十分简单，首先有给出一个长度为n的序列，最大值不超过m。
# 小团和小美各自选择一个[1,m]之间的整数，设小美选择的是l，小团选择的是r，我们认为两个人是默契的需要满足以下条件:
# 1. l 小于等于r。
# 2. 对于序列中的元素x，如果0<x<l,或r<x<m+1,则x按其顺序保留下来，要求保留下来的子序列单调不下降。
# 小团为了表现出与小美最大的默契，因此事先做了功课，他想知道能够使得两人默契的二元组<l,r>一共有多少种。
# 我们称一个序列A为单调不下降的，当且仅当对于任意的i>j,满足A_i>=A_j。
# 输入描述
# 输入第一行包含两个正整数m和n，表示序列元素的最大值和序列的长度。(1<=n,m<=100000)
# 输入第二行包含n个正整数，表示该序列。
# 输出描述
# 输出仅包含一个整数，表示能使得两人默契的二元组数量。
# 样例输入
# 5 5
# 4 1 4 1 2
# 样例输出
# 10

if __name__ == '__main__':
    while True:
        try:
            m, n = map(int, input().split())
            array = list(map(int, input().split()))
            if sorted(array) == array:
                print((1 + m) * m // 2)
            else:
                max_value = max(max(array), m)
                res = 0
                start = 1
                for i in range(1, max_value + 1):
                    # 标记右索引位置第一次满足
                    first = False
                    # 下一次满足条件的开始位置是从上次的开始位置之后开始
                    for j in range(start, max_value + 1):
                        temp = -1
                        flag = True
                        for k in range(n):
                            if array[k] < i or array[k] > j:
                                if temp == -1 or temp <= array[k]:
                                    temp = array[k]
                                else:
                                    flag = False
                                    break
                        # 第一次满足
                        if not first:
                            first = True
                            start = j
                        # 满足
                        if flag:
                            res += 1
                print(res)
        except:
            break




# if __name__ == '__main__':
#     while True:
#         try:
#             m, n = map(int, input().split())
#             array = list(map(int, input().split()))
#             if sorted(array) == array:
#                 print((1 + m) * m // 2)
#             else:
#                 max_value = max(max(array), m)
#                 res = 0
#                 for i in range(1, max_value + 1):
#                     for j in range(i, max_value + 1):
#                         temp = -1
#                         flag = True
#                         for k in range(n):
#                             if array[k] < i or array[k] > j:
#                                 if temp == -1 or temp <= array[k]:
#                                     temp = array[k]
#                                 else:
#                                     flag = False
#                                     break
#                         res += 1 if flag else 0
#                 print(res)
#         except:
#             break