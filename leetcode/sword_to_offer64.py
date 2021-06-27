# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

# 方法1 递归
class Solution:
    def sumNums(self, n: int) -> int:
        return 0 if n == 0 else n + self.sumNums(n - 1)