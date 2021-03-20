# 根据 逆波兰表示法，求表达式的值。
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
# 说明：
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for ele in tokens:
            if ele == "+":
                temp1, temp2 = stack.pop(), stack.pop()
                stack.append(temp1 + temp2)
            elif ele == "-":
                temp1, temp2 = stack.pop(), stack.pop()
                stack.append(temp2 - temp1)
            elif ele == "*":
                temp1, temp2 = stack.pop(), stack.pop()
                stack.append(temp1 * temp2)
            elif ele == "/":
                temp1, temp2 = stack.pop(), stack.pop()
                stack.append(int(temp2 / temp1))
            else:
                stack.append(int(ele))
        return stack[-1]


if __name__ == '__main__':
    s = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(tokens))