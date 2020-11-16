# 递归乘法
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if not A or not B:
            return 0
        if A < B:
            A, B = B, A
        return A + self.multiply(A, B - 1)