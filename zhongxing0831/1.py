# if __name__ == '__main__':
#     while True:
#         try:
#             n = int(input())
#             a = list(map(int, input().split()))
#             b = list(map(int, input().split()))
#             res = 0
#
#             def guibing_sort(l):
#                 global res
#                 if len(l) <= 1:
#                     return l
#                 array = []
#                 mid = len(l) // 2
#                 left = guibing_sort(l[:mid])
#                 right = guibing_sort(l[mid:])
#                 i, j = 0, 0
#                 while i < len(left) and j < len(right):
#                     if left[i] <= right[j]:
#                         array.append(left[i])
#                         i += 1
#                     else:
#                         array.append(right[j])
#                         res += len(left) - i
#                         j += 1
#                 if i < len(left):
#                     array += left[i:]
#                     res += len(right)
#                 if j < len(right):
#                     array += right[j:]
#                 return array
#
#
#             def func(a, b):
#                 res = 0
#                 i, j = 0, 0
#                 while i < len(a) and j < len(b):
#                     if a[i] <= b[j]:
#                         i += 1
#                     else:
#                         res += len(a) - i
#                         j += 1
#                 if i < len(a):
#                     res += len(b)
#                 return res
#
#             guibing_sort(a)
#             guibing_sort(b)
#             print(res + func(a, b))
#         except:
#             break


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            a = list(map(int, input().split()))
            b = list(map(int, input().split()))
            def func(a, b):
                res = 0
                i, j = 0, 0
                while i < len(a) and j < len(b):
                    if a[i] <= b[j]:
                        i += 1
                    else:
                        res += len(a) - i
                        j += 1
                return res

            print(func(a, b))
        except:
            break