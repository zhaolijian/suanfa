# 2
# 2
# 17 3
# 1
# 19

# 1
# 4
# 1 5 6 7
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        l = list(map(int, input().split()))
        length = len(l)
        if length <= 2:
            print(0)
        else:
            res = float('inf')

            def func(start, cha, init):
                global res
                temp = 0
                for i in range(2, len(l)):
                    if - 1 <= l[i] - (start + cha) <= 1:
                        if l[i] != start + cha:
                            temp += 1
                            start += cha
                    else:
                        temp = 0
                        break
                if temp == 0:
                    return
                else:
                    res = min(res, temp + init)


            for i in range(l[0] - 1, l[0] + 2):
                for j in range(l[1] - 1, l[1] + 2):
                    cha = j - i
                    init = 0
                    if i != l[0] and j != l[1]:
                        init = 2
                    elif i != l[0] or j != l[1]:
                        init = 1
                    func(j, cha, init)
            if res == float('inf'):
                print(-1)
            else:
                print(res)


# if __name__ == '__main__':
#     T = int(input())
#     for _ in range(T):
#         n = int(input())
#         l = list(map(int, input().split()))
#         length = len(l)
#         if length <= 2:
#             print(0)
#             continue
#         res = float('inf')
#         for j in range(-1, 2):
#             for k in range(-1, 2):
#                 cha = l[1] + k - l[0] + j
#                 now = l[1] + k
#                 cnt = abs(j)
#                 for i in range(1, n):
#                     if abs(l[i] - now) > 1:
#                         break
#                     elif l[i] != now:
#                         cnt += 1
#                     now += cha
#                 res = min(res, cnt)
#         if res == float('inf'):
#             print(-1)
#         else:
#             print(res)