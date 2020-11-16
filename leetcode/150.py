# 根据 逆波兰表示法，求表达式的值。
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
# 说明：
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

class Solution:
    def evalRPN(self, tokens) -> int:
        for i, ele in enumerate(tokens):
            if ele not in {'+', '-', '*', '/'}:
                tokens[i] = int(ele)
        stack = []
        for ele in tokens:
            if ele == '+':
                temp = stack.pop() + stack.pop()
                stack.append(temp)
            elif ele == '-':
                first = stack.pop()
                temp = stack.pop() - first
                stack.append(temp)
            elif ele == '*':
                temp = stack.pop() * stack.pop()
                stack.append(temp)
            elif ele == '/':
                first = stack.pop()
                temp = stack.pop() / first
                stack.append(int(temp))
            else:
                stack.append(ele)
        return stack[-1]


if __name__ == '__main__':
    s = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(tokens))