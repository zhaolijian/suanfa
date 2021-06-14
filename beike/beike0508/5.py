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
#         if index == n:
#             return False
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
#
# for _ in range(q):
#     # 判断能够使得橘子重量之和为s
#     s = int(input())
#     if func(weights, s, sum_weights, n):
#         print("YES")
#     else:
#         print("NO")