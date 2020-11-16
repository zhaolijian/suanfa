# 方法1， 比较好理解
if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            line = list(map(int, input().split()))
            K, d = map(int, input().split())
            value=0
            # 存储到每个元素的最大值
            fm=[[0 for j in range(K)] for i in range(n)]
            # 存储到每个元素的最小值
            fn=[[0 for j in range(K)] for i in range(n)]
            for i in range(n):
                fm[i][0] = fn[i][0] = line[i]
                for k in range(1, K):
                    for j in range(max(0, i-d), i):
                        fm[i][k] = max(fm[i][k], max(fm[j][k-1]*line[i],fn[j][k-1]*line[i]))
                        fn[i][k] = min(fn[i][k], min(fm[j][k-1]*line[i],fn[j][k-1]*line[i]))
                value = max(value,fm[i][K-1])
            print(value)
        except:
            break


# 方法2
# if __name__ == '__main__':
#     while True:
#         try:
#             n = int(input())
#             values = list(map(int, input().split()))
#             k, d = map(int, input().split())
#             table1 = [value for value in values]
#             table2 = [value for value in values]
#             for i in range(1, k):
#                 for j in range(n-1, i-1, -1):
#                     zmax = max(table1[max(0,j-d):j])
#                     fmin = min(table2[max(0,j-d):j])
#                     if values[j] >= 0:
#                         table1[j] = zmax * values[j]
#                         table2[j] = fmin * values[j]
#                     else:
#                         table1[j] = fmin * values[j]
#                         table2[j] = zmax * values[j]
#             print(max(table1))
#         except:
#             break