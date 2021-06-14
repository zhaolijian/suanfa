from bisect import bisect_right

l = list(map(int, input().split()))
n, q = l[0], l[1]
# n个橘子的重量
weights = list(map(int, input().split()))
sum_weights = sum(weights)
weights.sort()


def func(weights, s, sum_weights, n):
    if sum_weights == s:
        return True
    elif sum_weights < s:
        return False
    elif n == 1 and weights[0] > s:
        return False
    else:
        avg = sum_weights // n
        index = bisect_right(weights, avg)
        if index == n:
            return False
        temp = sum(weights[:index + 1])
        if index < n and weights[index] == avg:
            if func(weights[:index + 1], s, temp, index + 1):
                return True
            elif func(weights[index + 1:], s, sum_weights - temp, n - index - 1):
                return True
            return False
        else:
            if func(weights[:index], s, temp - weights[index], index):
                return True
            elif func(weights[index:], s, sum_weights - temp + weights[index], n - index):
                return True
            return False


for _ in range(q):
    # 判断能够使得橘子重量之和为s
    s = int(input())
    if func(weights, s, sum_weights, n):
        print("YES")
    else:
        print("NO")





# from bisect import bisect_right
#
# l = list(map(int, input().split()))
# n, q = l[0], l[1]
# # n个橘子的重量
# weigths = list(map(int, input().split()))
# weigths.sort()
# visisted = {}
#
#
# def func(weights, s):
#     sum_weights = sum(weights)
#     if sum_weights == s:
#         return True
#     elif sum_weights < s:
#         return False
#     elif len(weights) == 1 and weights[0] > s:
#         return False
#     else:
#         avg = sum(weights) // len(weights)
#         if avg in visisted:
#             return visisted[avg]
#         index = bisect_right(weights, avg)
#         if index < len(weights) and weights[index] == avg:
#             if func(weights[:index + 1], s):
#                 visisted[avg] = True
#                 return True
#             elif func(weights[index + 1:], s):
#                 visisted[avg] = True
#                 return True
#             visisted[avg] = False
#             return False
#         else:
#             if func(weights[:index], s):
#                 visisted[avg] = True
#                 return True
#             elif func(weights[index:], s):
#                 visisted[avg] = True
#                 return True
#             visisted[avg] = False
#             return False
#
#
# for _ in range(q):
#     # 判断能够使得橘子重量之和为s
#     s = int(input())
#     if func(weigths, s):
#         print("YES")
#     else:
#         print("NO")

# from bisect import bisect_right
#
# l = list(map(int, input().split()))
# n, q = l[0], l[1]
# # n个橘子的重量
# weights = list(map(int, input().split()))
# sum_weights = sum(weights)
# weights.sort()
#
#
# def func(weights, s, sum_weights, n):
#     if sum_weights == s:
#         return True
#     elif sum_weights < s:
#         return False
#     elif n == 1 and weights[0] > s:
#         return False
#     else:
#         avg = sum_weights // n
#         index = bisect_right(weights, avg)
#         temp = sum(weights[:index + 1])
#         if index < n and weights[index] == avg:
#             if func(weights[:index + 1], s, temp, index + 1):
#                 return True
#             elif func(weights[index + 1:], s, sum_weights - temp, n - index - 1):
#                 return True
#             return False
#         else:
#             if func(weights[:index], s, temp - weights[index], index):
#                 return True
#             elif func(weights[index:], s, sum_weights - temp + weights[index], n - index):
#                 return True
#             return False

#
# for _ in range(q):
#     # 判断能够使得橘子重量之和为s
#     s = int(input())
#     if func(weights, s, sum_weights, n):
#         print("YES")
#     else:
#         print("NO")



# l = list(map(int, input().split()))
# n, q = l[0], l[1]
# # n个橘子的重量
# weigths = list(map(int, input().split()))
# visisted = {}
#
#
# def func(weights, s):
#     sum_weights = sum(weights)
#     if sum_weights == s:
#         return True
#     elif sum_weights < s:
#         return False
#     elif len(weights) == 1 and weights[0] > s:
#         return False
#     else:
#         avg = sum(weights) // len(weights)
#         if avg in visisted:
#             return visisted[avg]
#         small_array, large_array = [], []
#         for ele in weights:
#             if ele <= avg:
#                 small_array.append(ele)
#             else:
#                 large_array.append(ele)
#         if func(small_array, s):
#             visisted[avg] = True
#             return True
#         if func(large_array, s):
#             visisted[avg] = True
#             return True
#         visisted[avg] = False
#         return False
#
#
# for _ in range(q):
#     # 判断能够使得橘子重量之和为s
#     s = int(input())
#     if func(weigths, s):
#         print("YES")
#     else:
#         print("NO")


# from bisect import bisect_right
#
# l = list(map(int, input().split()))
# n, q = l[0], l[1]
# # n个橘子的重量
# weigths = list(map(int, input().split()))
# weigths.sort()
# visisted = {}
#
#
# def func(weights, s):
#     sum_weights = sum(weights)
#     if sum_weights == s:
#         return True
#     elif sum_weights < s:
#         return False
#     elif len(weights) == 1 and weights[0] > s:
#         return False
#     else:
#         avg = sum(weights) // len(weights)
#         if avg in visisted:
#             return visisted[avg]
#         index = bisect_right(weights, avg)
#         if weights[index] == avg:
#             if func(weights[:index + 1], s):
#                 visisted[avg] = True
#                 return True
#             elif func(weights[index + 1:], s):
#                 visisted[avg] = True
#                 return True
#             visisted[avg] = False
#             return False
#         else:
#             if func(weights[:index], s):
#                 visisted[avg] = True
#                 return True
#             elif func(weights[index:], s):
#                 visisted[avg] = True
#                 return True
#             else:
#                 visisted[avg] = False
#                 return False
#
#
# for _ in range(q):
#     # 判断能够使得橘子重量之和为s
#     s = int(input())
#     if func(weigths, s):
#         print("YES")
#     else:
#         print("NO")



# from bisect import bisect_right
#
# l = list(map(int, input().split()))
# n, q = l[0], l[1]
# # n个橘子的重量
# weigths = list(map(int, input().split()))
# weigths.sort()
#
#
# def func(weights, s):
#     sum_weights = sum(weights)
#     if sum_weights == s:
#         return True
#     elif sum_weights < s:
#         return False
#     elif len(weights) == 1 and weights[0] > s:
#         return False
#     else:
#         avg = sum(weights) // len(weights)
#         index = bisect_right(weights, avg)
#         if index < len(weights) and weights[index] == avg:
#             if func(weights[:index + 1], s):
#                 return True
#             elif func(weights[index + 1:], s):
#                 return True
#             return False
#         else:
#             if func(weights[:index], s):
#                 return True
#             elif func(weights[index:], s):
#                 return True
#             else:
#                 return False
#
#
# for _ in range(q):
#     # 判断能够使得橘子重量之和为s
#     s = int(input())
#     if func(weigths, s):
#         print("YES")
#     else:
#         print("NO")