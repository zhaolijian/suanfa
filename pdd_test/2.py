# class Solution:
#     def solu(self, l):
#         temp_sum = sum(l)
#         avg = float(temp_sum) / 4
#         if avg % 1 != 0:
#             return 'NO'
#         else:
#             l.sort()
#             temp = 0
#             for m in range(len(l)):
#                 temp += l[m]
#                 if temp == avg:
#                     temp = 0
#             return 'YES' if temp == 0 else 'NO'

# if __name__ == '__main__':
#     n = int(input())
#     for _ in range(n):
#         l = list(map(int, input().split()))
#         l = l[1:]
#         temp_sum = sum(l)
#         avg = float(temp_sum) / 4
#         if avg % 1 != 0:
#             print('NO')
#         else:
#             l.sort()
#             temp = 0
#             for m in range(len(l)):
#                 temp += l[m]
#                 if temp == avg:
#                     temp = 0
#             if temp == 0:
#                 print('YES')
#             else:
#                 print('NO')


class Solution:
    def solu(self, n, l):
        res = []
        for i in range(n):
            l[i].sort()
            avg = float(sum(l[i])) / 4
            if avg % 1 != 0:
                res.append('NO')
            else:
                # 凑平均值
                temp = 0
                temp_array = []
                k = 0
                while k < 4:
                    for j in range(len(l[i]) - 1, -1, -1):
                        temp_array.append(j)
                        temp += l[i][j]
                        if temp == avg:
                            for key in temp_array:
                                l[i].pop(key)
                            temp_array = []
                            temp = 0
                            break
                        elif temp > avg:
                            temp -= l[i][j]
                            temp_array.pop()
                    k += 1
                res.append('YES' if not l[i] else 'NO')
        return res


if __name__ == '__main__':
    s = Solution()
    n = int(input())
    array = []
    for _ in range(n):
        l = list(map(int, input().split()))
        l = l[1:]
        array.append(l)
    result = s.solu(n, array)
    for temp in result:
        print(temp)


# if __name__ == '__main__':
#     n = int(input())
#     l = []
#     for _ in range(n):
#         temp = list(map(int, input().split()))
#         temp = temp[1:]
#         l.append(temp)
#     res = []
#     for i in range(n):
#         temp_sum = sum(l[i])
#         avg = float(temp_sum) / 4
#         if avg % 1 != 0:
#             res.append('NO')
#         else:
#             l[i].sort()
#             temp = 0
#             for m in range(len(l[i])):
#                 temp += l[i][m]
#                 if temp == avg:
#                     temp = 0
#             res.append('YES' if temp == 0 else 'NO')
#     for temp in res:
#         print(temp)