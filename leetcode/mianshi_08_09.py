# 括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。
class Solution:
    def generateParenthesis(self, n: int):
        # 前缀字符串、剩余左括号数、剩余右括号数
        def func(str, l, r):
            if len(str) == 2 * n:
                res.append(str)
                return
            if l > r:
                return
            elif l == r:
                func(str + "(", l - 1, r)
            else:
                if l > 0:
                    func(str + "(", l - 1, r)
                func(str + ")", l, r - 1)

        res = []
        func("", n, n)
        return res


if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.generateParenthesis(n))