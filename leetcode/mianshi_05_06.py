# 整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        i = 0
        res = 0
        while i < 32:
            if A & (1 << i) != B & (1 << i):
                res += 1
            i += 1
        return res