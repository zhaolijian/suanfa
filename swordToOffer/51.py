# 笨法，竟然能过。。。
# class Solution:
#     def multiply(self, A):
#         B = []
#         for i in range(len(A)):
#             temp = 1
#             for j in range(len(A)):
#                 if i == j:
#                     continue
#                 temp *= A[j]
#             B.append(temp)
#         return B


class Solution:
    def multiply(self, A):
        if not A:
            return []
        B = [0 for i in range(len(A))]
        B[0] = 1
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        for j in range(len(A) - 1, 0, -1):
            temp *= A[j]
            B[j - 1] *= temp
        return B