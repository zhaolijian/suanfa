# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。


# dfs
class Solution:
    def generateParenthesis(self, n: int):
        def func(number1, number2, already):
            if number1 == 0 and number2 == 0:
                res.append(already)
                return
            # number2剩下的只能大于等于number1
            if number1 == number2:
                func(number1 - 1, number2, already + "(")
            elif number1 < number2:
                if number1 > 0:
                    func(number1 - 1, number2, already + "(")
                func(number1, number2 - 1, already + ")")

        res = []
        func(n, n, "")
        return res