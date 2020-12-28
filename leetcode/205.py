# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。


# 方法1 更好
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if (s[i] in s2t and s2t[s[i]] != t[i]) or (t[i] in t2s and t2s[t[i]] != s[i]):
                return False
            if s[i] not in s2t:
                s2t[s[i]] = t[i]
            if t[i] not in t2s:
                t2s[t[i]] = s[i]
        return True


# 方法2
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c_s = defaultdict(list)
        c_t = defaultdict(list)
        for i, ele in enumerate(s):
            c_s[ele].append(i)
        for j, ele in enumerate(t):
            c_t[ele].append(j)
        if len(c_s.keys()) != len(c_t.keys()):
            return False
        array_s = set()
        array_t = set()
        for key in c_s.keys():
            array_s.add(tuple(sorted(c_s[key])))
        for key in c_t.keys():
            array_t.add(tuple(sorted(c_t[key])))
        return array_s == array_t


if __name__ == '__main__':
    s = Solution()
    ss = "egg"
    t = "add"
    print(s.isIsomorphic(ss, t))