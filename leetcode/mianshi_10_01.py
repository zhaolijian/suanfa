# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
# 初始化 A 和 B 的元素数量分别为 m 和 n。


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        cur_B = n - 1
        cur_A = m - 1
        cur = len(A) - 1
        while cur_A >= 0 and cur_B >= 0:
            if A[cur_A] > B[cur_B]:
                A[cur] = A[cur_A]
                cur_A -= 1
            else:
                A[cur] = B[cur_B]
                cur_B -= 1
            cur -= 1
        while cur_B >= 0:
            A[cur_B] = B[cur_B]
            cur_B -= 1