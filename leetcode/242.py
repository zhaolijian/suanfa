# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。


# 方法1
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        s2 = Counter(t)
        return s1 == s2


# 方法2
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        array = [0] * 26
        for i in range(len_s):
            array[ord(s[i]) - ord('a')] += 1
        for i in range(len_t):
            array[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if array[i]:
                return False
        return True
