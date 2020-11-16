# 无重复字符串的排列组合
# 前缀、剩下字符串
class Solution:
    def permutation(self, S: str) -> List[str]:
        def func(s, rest):
            if not rest:
                res.append(s)
                return
            for i in range(len(rest)):
                func(s + rest[i], rest[:i] + rest[i + 1:])

        length = len(S)
        res = []
        for i in range(length):
            func(S[i], S[:i] + S[i + 1:])
        return res