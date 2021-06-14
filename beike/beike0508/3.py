# l = list(map(int, input().strip().split()))
# # 序列的长度、要判断的元素
# n, k = l[0], l[1]
# array = list(map(int, input().strip().split()))
# left, right = 0, 0
# number_large, number_small = 0, 0
# res = 0
# while right < n:
#     if array[right] > k:
#         number_large += 1
#     else:
#         number_small += 1
#     if number_large > number_small:
#         res = max(res, right - left + 1)
#     else:
#         while left < right:
#             if array[left] > k:
#                 number_large -= 1
#             else:
#                 number_small -= 1
#             left += 1
#             if number_large > number_small:
#                 left -= 1
#                 break
#         left += 1
#     right += 1
# print(res)


l = list(map(int, input().strip().split()))
# 序列的长度、要判断的元素
n, k = l[0], l[1]
array = list(map(int, input().strip().split()))
res = 0
for i in range(n):
    number_large, number_small = 0, 0
    for j in range(i, n):
        if array[j] > k:
            number_large += 1
        else:
            number_small += 1
        if number_large > number_small:
            res = max(res, j - i + 1)
print(res)