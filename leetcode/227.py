# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        preflag = "+"
        number = 0
        # 如果s最后不加一个非数字非空格字符的话，s中的最后一个数字不会处理
        s += "&"
        for ele in s:
            if ele == " ":
                continue
            elif "0" <= ele <= "9":
                number = number * 10 + int(ele)
            else:
                if preflag == "+":
                    stack.append(number)
                elif preflag == "-":
                    stack.append(-number)
                elif preflag == "*":
                    stack.append(stack.pop() * number)
                elif preflag == "/":
                    # 这不能使用stack.pop() // number, 当stack.pop()为负数的时候，比如-3//2 = -2,错误，使用int方法向上区政府
                    stack.append(int(stack.pop() / number))
                number = 0
                preflag = ele
        return sum(stack)


if __name__ == '__main__':
    print((-3) / 2)
    print(int((-3) / 2))
    print(s.calculate(ss))