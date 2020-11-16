# 汉诺塔问题
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        def move(n, A, B, C):
            if n == 1:
                C.append(A[-1])
                A.pop()
                return
            else:
                move(n - 1, A, C, B)
                C.append(A[-1])
                A.pop()
                move(n - 1, B, A ,C)
        move(len(A), A, B, C)