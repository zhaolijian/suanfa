# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> str:
        c = Counter(s)
        for ele in s:
            if c[ele] == 1:
                return ele
        return " "
