# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j = len(num1) - 1, len(num2) - 1
        temp = 0
        while i >= 0 or j >= 0:
            val1 = int(num1[i]) if i >= 0 else 0
            val2 = int(num2[j]) if j >= 0 else 0
            number = val1 + val2 + temp
            if number < 10:
                temp = 0
                res = str(number) + res
            else:
                temp = 1
                res = str(number % 10) + res
            i -= 1
            j -= 1
        if temp:
            res = "1" + res
        return res