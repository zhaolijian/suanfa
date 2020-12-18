# 给定两个字符串 s 和 t，它们只包含小写字母。
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 请找出在 t 中被添加的字母。


# 位运算
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ele in s:
            res ^= ord(ele)
        for ele in t:
            res ^= ord(ele)
        return chr(res)


#ASCII码之和的差
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ele in t:
            res += ord(ele)
        for ele in s:
            res -= ord(ele)
        return chr(res)


# 哈希表
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s, counter_t = Counter(s), Counter(t)
        for key in counter_t.keys():
            if key not in counter_s.keys() or counter_t[key] > counter_s[key]:
                return key


# 桶计数
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        array = [0] * 26
        for ele in s:
            array[ord(ele) - ord('a')] += 1
        for ele in t:
            array[ord(ele) - ord('a')] -= 1
        for i in range(26):
            if array[i] < 0:
                return chr(ord('a') + i)