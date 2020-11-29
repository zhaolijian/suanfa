# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 如果不能形成任何面积不为零的三角形，返回 0。


class Solution:
    def largestPerimeter(self, A) -> int:
        length = len(A)
        A.sort(reverse=True)
        for i in range(length - 2):
            if A[i + 1] + A[i + 2] > A[i]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0