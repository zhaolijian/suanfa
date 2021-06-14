# 输入一个字符串，打印出该字符串中字符的所有排列。
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。


# 方法1 dfs+剪枝
# 每次确定一个位置，从0下标开始
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            # 该位置上已经出现的元素
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换
        dfs(0)
        return res


# 方法2 普通dfs
class Solution:
    def permutation(self, s: str) -> List[str]:
        res = set()
        def func(already, rest):
            if not rest:
                res.add(already)
            for i, ele in enumerate(rest):
                func(already + ele, rest[:i] + rest[i + 1:])
        func("", s)
        return list(res)