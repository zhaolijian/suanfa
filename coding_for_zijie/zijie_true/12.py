# 题目描述
# 给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
# 区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。
# 如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:
# [6] = 6 * 6 = 36;
# [2] = 2 * 2 = 4;
# [1] = 1 * 1 = 1;
# [6,2] = 2 * 8 = 16;
# [2,1] = 1 * 3 = 3;
# [6, 2, 1] = 1 * 9 = 9;
# 从上述计算可见选定区间 [6] ，计算值为 36， 则程序输出为 36。
# 区间内的所有数字都在[0, 100]的范围内;
# 输入描述:
# 第一行输入数组序列长度n，第二行输入数组序列。
# 对于 50%的数据,  1 <= n <= 10000;
# 对于 100%的数据, 1 <= n <= 500000;
# 输出描述:
# 输出数组经过计算后的最大值。

# 输入
# 3
# 6 2 1
# 输出
# 36


n = int(input())
array = list(map(int, input().split()))
stack = [[0, 0]]
left, right = 0, 0
res = 0
for ele in array:
    while stack[-1][0] > ele:
        top = stack.pop()
        left = top[1]
        res = max(res, top[0] * (right - top[1]))
    right += ele
    stack.append([ele, left])
    left = right
while stack:
    top = stack.pop()
    res = max(res, top[0] * (right - top[1]))
print(res)


# 超时，过70
# n = int(input())
# array = list(map(int, input().split()))
# s = sorted(list(set(array)))
# res = 0
# for ele in s:
#     sum_number = 0
#     min_val = 100
#     for j in range(n):
#         if array[j] >= ele:
#             sum_number += array[j]
#             min_val = min(min_val, array[j])
#             res = max(res, min_val * sum_number)
#         else:
#             min_val = 100
#             sum_number = 0
# print(res)


# 超时 过30
# n = int(input())
# array = list(map(int, input().split()))
# # 累加和数组
# sum_array = [0]
# for i in range(n):
#     sum_array.append(sum_array[-1] + array[i])
# res = 0
# for i in range(n):
#     min_val = array[i]
#     for j in range(i, n):
#         min_val = min(min_val, array[j])
#         res = max(res, min_val * (sum_array[j + 1] - sum_array[i]))
# print(res)