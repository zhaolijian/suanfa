# 给出两个有序的整数数组 和 ，请将数组 合并到数组 中，变成一个有序的数组
# 注意：
# 可以假设 数组有足够的空间存放 数组的元素， 和 中初始的元素数目分别为 和

# 从后往前遍历，大的放到后面
class Solution:
    def merge(self , A, m, B, n):
        index = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1
            index -= 1
        if j >= 0:
            A[: j + 1] = B[: j + 1]