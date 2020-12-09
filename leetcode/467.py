# 把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，所以 s 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 
# 现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p 的不同的非空子串的数目。 
# 注意: p 仅由小写的英文字母组成，p 的大小可能超过 10000。


# 哈希表
from collections import defaultdict
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        init = defaultdict(int)
        p = "*" + p
        number = 1
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i - 1]) in {1, -25}:
                number += 1
            else:
                number = 1
            init[p[i]] = max(init[p[i]], number)
        return sum(init.values())


# from collections import defaultdict
# class Solution:
#     def findSubstringInWraproundString(self, p: str) -> int:
#         if not p:
#             return 0
#         len_mapper = defaultdict(int)
#         len_mapper[p[0]] = 1
#         w = 1
#         for i in range(1,len(p)):
#             if ord(p[i])-ord(p[i-1]) == 1 or ord(p[i])-ord(p[i-1]) == -25:
#                 w += 1
#             else:
#                 w = 1
#             len_mapper[p[i]] = max(len_mapper[p[i]], w)
#         return sum(len_mapper.values())
