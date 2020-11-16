# 计算最少出列多少位同学，使得剩下的同学排成合唱队形
# 说明：
# N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
# 合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，
# 则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。
# 你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
# 注意不允许改变队列元素的先后顺序
# 请注意处理多组输入输出！


# 方法1 二分查找 时间复杂度O(nlogn)
# from bisect import bisect_left
#
#
# def func(array, dp):
#     # 表示该人及其左侧的人数
#     dp += [1]
#     b = [float('inf')] * len(array)
#     b[0] = array[0]
#     for i in range(1, len(array)):
#         pos = bisect_left(b, array[i])
#         b[pos] = array[i]
#         dp += [pos + 1]
#     return dp
#
#
# if __name__ == '__main__':
#     while True:
#         try:
#             N = int(input())
#             array = list(map(int, input().split()))
#             length = len(array)
#             l = func(array, [])
#             r = func(array[::-1], [])[::-1]
#             res = 0
#             for i in range(length):
#                 res = max(res, l[i] + r[i] - 1)
#             print(length - res)
#         except:
#             break


# 方法2 普通的dp，时间复杂度O(n^2)
# def func(array, length):
#     dp = [1] * length
#     for i in range(length):
#         for j in range(i):
#             if array[j] < array[i]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     return dp
#
#
# if __name__ == '__main__':
#     while True:
#         try:
#             N = int(input())
#             array = list(map(int, input().split()))
#             length = len(array)
#             l = func(array, length)
#             r = func(array[::-1], length)[::-1]
#             res = 0
#             for i in range(length):
#                 res = max(res, l[i] + r[i] - 1)
#             print(length - res)
#         except:
#             break