# 字符串轮转
# 思路，将两个s1拼接，如果s2是s1旋转得到的，则在两个s1拼接字符串中一定能找到s2
# 方法1 使用find方法
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and (s1 + s1).find(s2) != -1

# 方法2 不使用find方法
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True
        if len(s1) != len(s2):
            return False
        length = len(s2)
        s1 += s1
        for i in range(length):
            if s2 == s1[i: i + length]:
                return True
        return False